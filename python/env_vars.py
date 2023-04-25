
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# Set your Spotify API credentials
client_id = "3c70b159bb9848ca890755bf3083e080"
client_secret = "578f8808a62d4b92b5d8387d61c33432"
redirect_uri = "http://localhost:8888/callback/"

# Set the required scope(s)
scope = "user-library-read"

# Set up client credentials for public data access
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Set up OAuth 2.0 for user-specific data access
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)

# Create a spotipy.Spotify instance with both client credentials and OAuth 2.0 authentication
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth_manager=auth_manager)



# Now lets work with our playlist
playlist_id = "1pDpruzoY7JvPBq2CJujFs"
# Got it baby whohhh
playlist = sp.playlist(playlist_id)

print(f"Playlist name: {playlist['name']}")
print(f"Total tracks: {playlist['tracks']['total']}")
