
from mongoengine import *

# Connect to MongoDB
connect('dbtest')

# Define the Tlist EmbeddedDocument
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the Test Document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Example data entry
data = [('test1', "a"), ('test2', "b"), ('test3', "c")]

# Create and save Test instances with Tlist
for tag, ref in data:
    test = Test(tag=tag)  # Assign tag on creation
    tlist = Tlist(ref=ref)  # Assign ref on creation
    test.tlists.append(tlist)
    test.save()
