import pymongo
client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
test = mydb['test']
test.insert_one({'name': 'Jan', 'sex': 'man', 'grade': 89})
