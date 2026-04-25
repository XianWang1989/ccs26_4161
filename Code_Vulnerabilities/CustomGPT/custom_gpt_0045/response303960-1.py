
from mongoengine import connect, Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField

# Connect to the MongoDB database
connect('dbtest')

# Define a document class
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define an embedded document class
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Create and save documents
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test(tag=i[0])
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
