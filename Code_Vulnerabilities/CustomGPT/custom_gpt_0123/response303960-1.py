
from mongoengine import *

# Connect to the database
connect('dbtest')

# Define the embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the main document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Sample data insertion
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist(ref=i[1])  # Create Tlist instance directly
    test.tlists.append(tlist)
    test.save()
