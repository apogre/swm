import pymongo
import json

conn = pymongo.MongoClient()
collection = conn['db']['user_info']

for doc in json.load(open('users.json')):
    new_doc = {k: v for k, v in doc.iteritems() if k in ('email', 'username', 'avatar')}
    collection.update({'_id': doc['_id']}, {'$set': new_doc})


  mongoexport -h localhost -d local -c user_info --type=csv -f "id,screen_name,name,created_at,time_zone,lang,location,friends_count,description,statuses_count,verified,followers_count,favourites_count" -o full_data1.csv