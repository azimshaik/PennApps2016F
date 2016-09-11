from pymongo import Connection
connection = Connection()
connection = Connection('localhost', 27017)
db = connection.test
collection = db.student
for post in collection.find():
        print post
