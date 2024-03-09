from spotify import copy_playlist, copy_user_playlists
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()

  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument("-u", "--user")
  group.add_argument("-p","--playlist")

  args = parser.parse_args()

  if args.user:
    copy_user_playlists(args.user, silent=False)
  
  if args.playlist:
    copy_playlist(args.playlist, silent= False)



