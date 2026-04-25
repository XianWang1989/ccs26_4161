
from mongoengine import *
from mongoengine import connect, Document, StringField, ListField, EmbeddedDocumentField, EmbeddedDocument

# Connect to the MongoDB database
connect('dbtest')

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Create and save documents to the database
for i in [('test1', "a"), ('test2', "b"), ('test3", "c"), 
          ('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
