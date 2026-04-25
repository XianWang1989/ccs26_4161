
from mongoengine import *

# Connect to the database
connect('dbtest')

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Adding data
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test(tag=i[0])
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
