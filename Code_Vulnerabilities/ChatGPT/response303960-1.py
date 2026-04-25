
from mongoengine import *

# Connect to the MongoDB database named 'dbtest'
connect('dbtest')

# Define the main document class
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the embedded document class
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Insert multiple Test documents, each containing a list of Tlists
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
