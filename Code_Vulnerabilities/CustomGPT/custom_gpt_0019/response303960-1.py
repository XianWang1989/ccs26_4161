
from mongoengine import *
from mongoengine import Document, StringField, ListField, EmbeddedDocumentField, EmbeddedDocument

# Connect to MongoDB database
connect('dbtest')

# Define the Tlist embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the main Test document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Create and save Test documents
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"), ('test1', "a"),
          ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
