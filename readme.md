# FAQ

### **Why is this useful?** <br>
Spotify doesnt let users to easily copy another user's playlists, you are able to listen to them - however you are unable to edit the playlist in any way to truly make it your own. This script allows you to 'take ownership' over other user's playlists.

### **How can this get me free spotify premium?** <br>
With very minimal effort at intervals of once every ~1-3 months, you can effectively achieve free spotify premium by utilising spotify's consistent 'free trial' promotions in combination with this script.
  - Create a [new account](https://www.spotify.com/signup)
  - Sign up to a free trial plan using a card that you have not used to sign up with before
    - (you can easily get fresh virtual cards with [revolut](https://www.revolut.com/))
  - It is recommended you 'cancel' the plan immediately so you dont accidentally get charged
    - You will have premium for the entirety of the free trial period even if you cancel the subscription instantly. Ignore any messages that say otherwise while you are cancelling.
  - Use this script to copy the playlists from your previous account to the new one
  - Once the trial period is over, repeat!

# Usage
Once [setup](#Setup) is complete: <br>

### Commands

- `python main.py -u <target user id>` Copies all playlists from the account of the user specified to your account<br>
- `python main.py -p <playlist id>` Copies the playlist specified to your account

### Locating ID's

You can find a `user id` or `playlist id` by navigating to either the 'playlist page' of the target playlist or 'profile page' of the target user. Once there, inspect the page's url, and copy the string of characters at the end.

![PID](https://raw.githubusercontent.com/FlynnHillier/spotify-playlist-copy/media/media/PID.png)

![UID](https://raw.githubusercontent.com/FlynnHillier/spotify-playlist-copy/media/media/UID.png)




# Setup
### Installation
1. Install [python](https://www.python.org/downloads/) (with pip)
2. Clone this project
3. in the project's directory run `pip install -r requirements.txt`

### Spotify developer api
1. To gain access to the spotify developer api [register here](https://developer.spotify.com/dashboard).<br>
   - You may use any spotify account with a verified email address to register for this, it *does not* need to be the same account you wish to copy a playlist to/from.

2. Once you have registered for access to the spotify developers api, [create an app](https://developer.spotify.com/dashboard/create).
    - We will register the account that we wish to copy playlists to, to this app. This is done so that our script has the proper permissions needed to modify the target account's playlists.
    - The 'App name' , 'App description' & 'website' can all be any random values. They do not matter.
    - 'redirect URI' does not matter either, but it is suggested to put something like "http://localhost:5000"


3. Navigate to your app's dashboard (you can find a link to that [here](https://developer.spotify.com/dashboard)). 
    - Navigate to 'Settings' > 'User Management'.
    - add a user <ins>with the email address of the account you intend to copy playlists to</ins> (name does not matter)
    - When the application is first ran, you will be prompted to authorize your app for your account, this is only done once. 
    - If you wish to copy playlists to another account in the future this step must be repeated for said account.
      - You may also need to delete the `.cache` file to re-prompt app authorization for the new account. This way the script will copy the playlists to the correct account.

### Config.json
Fill out the config.json file in your project's directory.

- `OAUTH`
    - `clientID` : the client ID from your spotify developer app
    - `clientSecret` : the client secret from your spotify developer app
    - `redirectURI` : the redirectURI from your spotify developer app

A link to the the app dashboard containing the values needed should be present [here](https://developer.spotify.com/dashboard)
