import tweepy
from pymongo import MongoClient
import json
import time
import cPickle as pickle

client = MongoClient()
col = client.local.lfc_user_following


consumer_key = 'v56jERn7xh9xRoIxX2JGSeeKl'
consumer_secret='Oq10zcJC0SomweK790KRZoFT7CuudiotePqwBJZPGPM2BA09wX'
access_token='300823393-ksw43zLieQopGX1YGjmiwyigNpHYAbHSs5P8r17d'
access_token_secret='YiWcTljsahRdh243kDj4NZrx4AErYPMJ2XWeIEWaiQKA0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
error = []

def get_usernames(names):
	test = api.lookup_users(screen_names=names)
	data = [user._json for user in test]
	col.insert(data)

with open('lfc.json') as js:
	user_id = json.load(js)
	# print user_id
	id_follower = user_id['Followers']
	# print len(id_follower)
	while len(id_follower) !=0:
		print len(id_follower)
		try:
			names = id_follower[:99]
			get_usernames(names)
			time.sleep(5)
		except:
			error.append(id_follower[:99])
		del id_follower[:99]

if error:
	print error
	with open('error_follower_id.txt','wb') as fp:
		pickle.dump(error,fp)