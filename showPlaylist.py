import spotipy 
import sys
import spotipy
import spotipy.util as util
#export SPOTIPY_CLIENT_ID='6784b2a327f34385ac1390889259ee2e'
#export SPOTIPY_CLIENT_SECRET = 'e08b40c19d1940ac9d76fad6f31b2269'
#export SPOTIPY_REDIRECT_URI = 'https://google.com/'


#scope = 'user-library-read'

#username = 

#token = util.prompt_for_user_token(username, scope)

#util.prompt_for_user_token(username,scope,client_id='1110922843',client_secret='your-app-redirect-url',redirect_uri='your-app-redirect-url')

#davids ID 	1110922843
#my username  https://open.spotify.com/user/21qshqo4beqqk7bzu7gfnctqy?si=0ZRnGWxjTLmUwUPAYm_zsQ
#client ID 	  spotify:user:21qshqo4beqqk7bzu7gfnctqy
 

#"https://docs.google.com/spreadsheets/d/140gFylIoLs_dkUz0OKkoWEj5eFJLc9jc6SgInYWWqZ8/edit?ts=5b741e67#gid=1070637439"

#"http://"

#user_playlist(user, playlist_id=None, fields=None)

def setcredentials(username):
	pass

def showplaylistdata():
	pass



if __name__ == '__main__':

	#prompt the user for their token to authenticate
	username = "21qshqo4beqqk7bzu7gfnctqy?si=0ZRnGWxjTLmUwUPAYm_zsQ"
	scope = 'user-library-read' 
	#scope = 'playlist-read-private'
	#token = util.prompt_for_user_token(username)
	#sp = spotipy.Spotify(auth=token)
	print(username)
	#scope = 'user-library-read'
	#SPOTIPY_CLIENT_ID='6784b2a327f34385ac1390889259ee2e'
	#SPOTIPY_CLIENT_SECRET = 'e08b40c19d1940ac9d76fad6f31b2269'
	#SPOTIPY_REDIRECT_URI = 'https://google.com/'

    #if len(sys.argv) > 1:
    #    username = sys.argv[1]
    #else:
    #    print "Usage: %s username" % (sys.argv[0],)
    #    sys.exit()

	token = util.prompt_for_user_token(username,scope=scope , client_id='6784b2a327f34385ac1390889259ee2e', client_secret='e08b40c19d1940ac9d76fad6f31b2269', redirect_uri='http://localhost:8888/callback/') #scope
	if token:
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_saved_tracks()
		for item in results['items']:
			track = item['track']
			print(track['name'] + ' - ' + track['artists'][0]['name'])
			#get the top 10 tracks of my spotify

		results = sp.current_user_playlists(limit=3)
		for item in results['items']:
			print(item)
			#get top 3 playlists

		#user_playlist(user, playlist_id=None, fields=None)
				#get playlist 
	else:
		print("Can't get token for", username)