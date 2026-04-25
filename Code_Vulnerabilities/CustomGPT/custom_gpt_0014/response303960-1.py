
from mongoengine import *

# Connect to your database
connect('dbtest')

# Define Document classes
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Create and save instances
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
