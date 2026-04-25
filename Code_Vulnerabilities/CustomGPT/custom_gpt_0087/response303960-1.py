
from mongoengine import connect, Document, StringField, ListField, EmbeddedDocumentField, EmbeddedDocument

# Connect to the database
connect('dbtest')

# Define the main document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Define the embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Sample data to save in the database
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"),
          ('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
