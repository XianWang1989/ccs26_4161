
from mongoengine import *

# Connect to the MongoDB database
connect('dbtest')

# Define the Test Document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the Tlist EmbeddedDocument
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Insert sample data
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
