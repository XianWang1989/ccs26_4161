
from mongoengine import *

# Connect to your database
connect('dbtest')

# Define your document models
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Populate the database
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
