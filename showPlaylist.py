import spotipy 
import sys
import spotipy
import spotipy.util as util


#scope = 'user-library-read'

#username = 

#token = util.prompt_for_user_token(username, scope)

#util.prompt_for_user_token(username,scope,client_id='1110922843',client_secret='your-app-redirect-url',redirect_uri='your-app-redirect-url')

#davids ID 	1110922843
#my username  https://open.spotify.com/user/21qshqo4beqqk7bzu7gfnctqy?si=0ZRnGWxjTLmUwUPAYm_zsQ
#client ID 	  spotify:user:21qshqo4beqqk7bzu7gfnctqy
 

#"https://docs.google.com/spreadsheets/d/140gFylIoLs_dkUz0OKkoWEj5eFJLc9jc6SgInYWWqZ8/edit?ts=5b741e67#gid=1070637439"

#"http://localhost:8888/callback"

#user_playlist(user, playlist_id=None, fields=None)

def setcredentials(username):
	pass

def showplaylistdata():
	pass



if __name__ == '__main__':

#prompt the user for their token to authenticate
	username = "21qshqo4beqqk7bzu7gfnctqy?si=0ZRnGWxjTLmUwUPAYm_zsQ"
	token = util.prompt_for_user_token(username)
	sp = spotipy.Spotify(auth=token)
	print(username)

	export SPOTIPY_CLIENT_ID='your-spotify-client-id'
    export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
    export SPOTIPY_REDIRECT_URI='your-app-redirect-url'