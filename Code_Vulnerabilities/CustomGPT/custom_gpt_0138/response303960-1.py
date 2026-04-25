
from mongoengine import *

# Connect to MongoDB
connect('dbtest')

# Define the Document and EmbeddedDocument classes
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Insert data
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"), ('test1', "a"),
          ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
