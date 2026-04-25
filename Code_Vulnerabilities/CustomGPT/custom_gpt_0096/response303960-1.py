
from mongoengine import *

# Connect to the MongoDB database
connect('dbtest')

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Inserting data into the database
data = [('test1', "a"), ('test2', "b"), ('test3', "c")]
for tag, ref in data:
    test = Test(tag=tag)
    tlist = Tlist(ref=ref)
    test.tlists.append(tlist)
    test.save()
