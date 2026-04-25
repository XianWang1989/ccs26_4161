
from mongoengine import *

# Connect to the database
connect('dbtest')

# Define the Tlist embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the Test document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Create and save Test documents
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test(tag=i[0])
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
