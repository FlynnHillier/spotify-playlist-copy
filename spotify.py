from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
from config import config

def __getSpotipyClient() -> Spotify:
  OAUTH = SpotifyOAuth(
    client_id=config["OAUTH"]["clientID"],
    client_secret=config["OAUTH"]["clientSecret"],
    redirect_uri=config["OAUTH"]["redirectURI"],
    open_browser=True,
    scope="playlist-modify-private,playlist-read-private,playlist-modify-public,user-library-modify,user-library-read"
  )

  return Spotify(
    client_credentials_manager=OAUTH
  )


spotipy = __getSpotipyClient()
me = spotipy.me()



def __user_exists_playlist(playlist_name:str) -> None | str:
  """Fetch existing playlist id for a user's playlist with the specified name

  Args:
      playlist_name (str): playlist name to query

  Returns:
      None | str: playlist id if is matching playlist is found, else None
  """
  offset = 0
  while True:
    existing = spotipy.user_playlists(me["id"], limit=50, offset=offset)
    for playlist in existing["items"]:
      if(playlist["name"] == playlist_name):
        return playlist["id"]
    
    if len(existing) < 50:
      break
    offset += 50
      
  return None


def __extract_playlist_track_ids(playlist) -> list[str]:
  """Given a playlist return all track ids contained within the playlist

  Args:
      playlist (spotipy playlist): the playlist to extract track ids from

  Returns:
      list[str]: a list of track ids (non-duplicate)
  """
  return list(set(map(lambda d : d["track"]["uri"], playlist["tracks"]["items"])))



def copy_playlist(playlist_id:str,
 target_user_existing_playlist : bool = True
 ) -> int:
  """copies the given playlist to the user's account

  Args:
      playlist_id (str): the id of the playlist to copy
      target_user_existing_playlist (bool, optional): If True, if a playlist with a name that matches the target playlist's name exists on the user's account - copy non-duplicate tracks into this playlist. Defaults to True.

  Returns:
      int: the number of tracks added
  """
  target = spotipy.playlist(playlist_id)

  tracks = __extract_playlist_track_ids(target)

  if target_user_existing_playlist and (existingID := __user_exists_playlist(target["name"])) != None:
    # target existing user playlist
    playlist = spotipy.user_playlist(me["id"], playlist_id=existingID)

    # Copy only tracks that are not already present in existing playlist
    existing_tracks = __extract_playlist_track_ids(playlist)
    _tracks = []
    for track in tracks:
      if track not in existing_tracks:
        _tracks.append(track)
    
    tracks = _tracks
  else:
    # create new user playlist
    playlist = spotipy.user_playlist_create(me["id"], target["name"])


  if(len(tracks) > 0):
    spotipy.playlist_add_items(playlist["id"], items=tracks)

  return len(tracks)