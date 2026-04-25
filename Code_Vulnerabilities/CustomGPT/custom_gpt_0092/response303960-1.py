
from mongoengine import *

# Connect to the database
connect('dbtest')

# Define the Test document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the Tlist embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Save sample records
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"), 
          ('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
