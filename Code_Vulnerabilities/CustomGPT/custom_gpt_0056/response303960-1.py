
from mongoengine import *

# Connect to your MongoDB database
connect('dbtest')

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Example data insertion
for i in [('test1', "a"), ('test2', "b")]:
    test = Test()
    test.tag = i[0]
    test.tlists.append(Tlist(ref=i[1]))
    test.save()
