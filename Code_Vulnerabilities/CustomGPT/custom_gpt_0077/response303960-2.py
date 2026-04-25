
from mongoengine import connect, Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField

# Connect to your MongoDB database
connect('dbtest')

# Define the Document class
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the Embedded Document class
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Create and save instances of the Document
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
