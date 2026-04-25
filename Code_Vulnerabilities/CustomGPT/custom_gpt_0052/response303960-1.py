
from mongoengine import *

# Connect to MongoDB
connect('dbtest')

# Define the embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the main document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Sample data to insert
data = [('test1', "a"), ('test2', "b"), ('test3', "c")]

# Insert data into the database
for i in data:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
