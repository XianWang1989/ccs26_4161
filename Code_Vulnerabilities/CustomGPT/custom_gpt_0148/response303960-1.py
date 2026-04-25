
from mongoengine import *

# Connect to the database
connect('dbtest')

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Sample data
data = [('test1', "a"), ('test2', "b"), ('test3', "c")]

# Create and save Test documents
for item in data:
    test = Test(tag=item[0])
    tlist = Tlist(ref=item[1])
    test.tlists.append(tlist)
    test.save()
