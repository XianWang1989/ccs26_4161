
from mongoengine import *

# Establish connection
connect('dbtest')

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Example data
data = [('test1', 'a'), ('test2', 'b'), ('test3', 'c')]

for tag, ref in data:
    test = Test(tag=tag)
    tlist = Tlist(ref=ref)
    test.tlists.append(tlist)
    test.save()
