
from mongoengine import *

# Connect to the MongoDB database
try:
    connect('dbtest')
except Exception as e:
    print(f"Failed to connect to the database: {e}")

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Create and save documents
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"), ('test1', "a"),
          ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
