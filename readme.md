# Setup instructions
Spotify developer api
---
1. To gain access to the spotify developer api [register here](https://developer.spotify.com/dashboard).<br>
   - You may use any spotify account with a verified email address to register for this, it *does not* need to be the same account you wish to copy a playlist to/from.

2. Once you have registered for access to the spotify developers api, [create an app](https://developer.spotify.com/dashboard/create).
    - We will register the account that we wish to copy playlists to, to this app. This is done so that our script has the proper permissions needed to modify the target account's playlists.
    - The 'App name' , 'App description' & 'website' can all be any random values. They do not matter.
    - 'redirect URI' does not matter either, but it is suggested to put something like "http://localhost:5000"


3. Navigate to your app's dashboard (you can find a link to that [here](https://developer.spotify.com/dashboard)). 
    - Navigate to 'Settings' > 'User Management'.
    - add a user <ins>with the email address of the account you intend to copy playlists to</ins> (name does not matter)
    - If you wish to copy playlists to another account in the future this step must be repeated for said account.

