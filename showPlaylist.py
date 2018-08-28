import spotipy 
import sys
import spotipy
import spotipy.util as util


def setcredentials(username):
	pass

def showplaylistdata():
	pass

def mytracks(sp):
	results = sp.current_user_saved_tracks()
	for item in results['items']:
		track = item['track']
		print(track['name'] + ' - ' + track['artists'][0]['name'])

def myplaylists(sp):
	results = sp.current_user_playlists(limit=10)
	for item in results['items']:
		print(item)

def officeplaylist(sp):
	results = sp.user_playlist('1110922843','3gftLZFZYjMYszOlsQIqeA',limit=600)
	#user_playlist_tracks()
	#for item in results['items']:
	#print(item)
	print(results)



if __name__ == '__main__':

	#prompt the user for their token to authenticate
	username = "21qshqo4beqqk7bzu7gfnctqy?si=0ZRnGWxjTLmUwUPAYm_zsQ"
	scope = 'user-library-read'
	cid = '6784b2a327f34385ac1390889259ee2e'
	cs = 'e08b40c19d1940ac9d76fad6f31b2269'
	ru = 'http://localhost:8888/callback/'
	

	token = util.prompt_for_user_token(username,scope=scope , client_id=cid, client_secret=cs, redirect_uri=ru) #scope
	if token:
		sp = spotipy.Spotify(auth=token)
		
		#mytracks(sp)
		#myplaylists(sp)
		#officeplaylist
		#spotify:user:1110922843
		#spotify:user:1110922843:playlist:3gftLZFZYjMYszOlsQIqeA
		#fields=None
		officeplaylist(sp)
		
	else:
		print("Can't get token for", username)

