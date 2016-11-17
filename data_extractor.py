import pymongo
import json

conn = pymongo.MongoClient()
collection = conn['db']['user_info']

for doc in json.load(open('users.json')):
    new_doc = {k: v for k, v in doc.iteritems() if k in ('email', 'username', 'avatar')}
    collection.update({'_id': doc['_id']}, {'$set': new_doc})