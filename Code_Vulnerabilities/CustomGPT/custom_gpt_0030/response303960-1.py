
from mongoengine import *

# Connect to the MongoDB database
connect('dbtest')

# Define the main document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Create instances and save them
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"), ('test1', "a"),
          ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]  # Set the tag
    tlist = Tlist()
    tlist.ref = i[1]  # Set the reference
    test.tlists.append(tlist)  # Append to the list
    test.save()  # Save the document
