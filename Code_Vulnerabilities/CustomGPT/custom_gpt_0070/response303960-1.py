
from mongoengine import *

# Connect to the database
connect('dbtest')

# Define the EmbeddedDocument Tlist
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the Document Test
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Create and save test documents
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
