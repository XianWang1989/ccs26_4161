
from mongoengine import *

# Connect to the database
connect('dbtest')

# Define the Test document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the Tlist embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Example data to insert
data = [('test1', "a"), ('test2', "b"), ('test3', "c"), 
        ('test1', "a"), ('test2', "b"), ('test3', "c")]

# Save Test documents
for i in data:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
