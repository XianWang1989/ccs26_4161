
from mongoengine import *

# Make sure you've installed pymongo correctly
# You can do this with: pip install pymongo mongoengine

connect('dbtest')

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Sample data to insert
data = [('test1', "a"), ('test2', "b"), ('test3', "c")]

for tag, ref in data:
    tlist = Tlist(ref=ref)
    test = Test(tag=tag, tlists=[tlist])
    test.save()
