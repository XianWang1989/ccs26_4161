
from mongoengine import *

connect('dbtest')  # Connect to the database

class Test(Document):
    tag = StringField(required=True)  # Define a required string field
    tlists = ListField(EmbeddedDocumentField('Tlist'))  # List of embedded documents

class Tlist(EmbeddedDocument):
    ref = StringField(required=True)  # Required reference field

# Loop to create and save Test documents with embedded Tlist documents
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]  # Set the tag
    tlist = Tlist()
    tlist.ref = i[1]  # Set the reference
    test.tlists.append(tlist)  # Append the embedded document
    test.save()  # Save the document
