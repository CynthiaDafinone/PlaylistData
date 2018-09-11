import spotipy 
import sys
import spotipy
import spotipy.util as util




def getUsername(sp,uid):
	#gets the usersname from a userID
	uno = uid2uno(uid)
	results = sp.user(uno)
	print(results['display_name'])


def uid2uno(uid):
	#converts from a userID to a usernumber 
	uno = uid.replace('spotify:user:','')
	return uno 

def tid2tno(tid):
	#coverts from a trackID to a tracknumber
	#tno = tid.replace('spotify:track:')
	pass


def getGenre(tid):
	#uses search function to return genre 
	#tno = tid2tno(tid)
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
	#results = sp.user_playlist('1110922843','3gftLZFZYjMYszOlsQIqeA',limit=600)
	offs = 0 
	for i in range(6):
		
		playlist = sp.user_playlist_tracks('1110922843','3gftLZFZYjMYszOlsQIqeA',fields=None, limit=100, offset=offs, market=None)
	#fields=None, limit=50, offset=0, market=None)
		offs = offs +100
		for item in playlist['items']:
			#print(item)
			 #date and time added 
			dateAdded = item['added_at']
			print(dateAdded)

			#uri of username -added by
			username = getUsername(sp,item['added_by']['uri'])
			print(username)

		
			#gets the name of each track 
			trackName = item['track']['name']
			print(trackName)

			#uri of track for genre search - for genre 
			trackURI = item['track']['uri'] 
			print(trackURI)
			#genre = getGenre (trackURI)

			#gets the name of each album 
			albumName = item['track']['album']['name']
			print(albumName)
			
			#gets the name of each artist
			artist = item['track']['album']['artists'][0]['name'] 
			print(artist) 
			
	#print(results)

	



if __name__ == '__main__':
	#spotify:user:1168610742
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
		getUsername(sp,'1121686703')
		
	else:
		print("Can't get token for", username)

#--------------
#Paramters needed

#date added 
#name of user who added song 
#song name 
#album name 
#artist
#genre * 
#tracklength*

#*metadata can be reached using the search function 

#pip install --upgrade google-api-python-client oauth2client