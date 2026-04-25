
from mongoengine import *

# Establish a connection to MongoDB
connect('dbtest')

class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Example data input
data_input = [('test1', "a"), ('test2', "b"), ('test3', "c"),
              ('test1', "a"), ('test2', "b"), ('test3', "c")]

for item in data_input:
    test = Test()
    test.tag = item[0]
    tlist = Tlist()
    tlist.ref = item[1]
    test.tlists.append(tlist)
    test.save()
