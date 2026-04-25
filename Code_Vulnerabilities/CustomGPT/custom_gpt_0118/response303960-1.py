
from mongoengine import *

# Connect to your MongoDB database
connect('dbtest')

# Define the Embedded Document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the main Document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Sample data insertion
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
