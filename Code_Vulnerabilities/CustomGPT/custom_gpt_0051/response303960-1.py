
from mongoengine import *

connect('dbtest')

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Create and save documents
for tag, ref in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test(tag=tag)
    tlist = Tlist(ref=ref)
    test.tlists.append(tlist)
    test.save()

print("Documents saved successfully!")
