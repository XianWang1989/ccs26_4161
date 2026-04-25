
from mongoengine import connect, Document, StringField, ListField, EmbeddedDocument, EmbeddedDocumentField

# Connect to MongoDB
connect('dbtest')

# Define Embedded Document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define Main Document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Insert data
sample_data = [('test1', "a"), ('test2', "b"), ('test3', "c")]

for tag, ref in sample_data:
    test = Test(tag=tag)
    tlist = Tlist(ref=ref)
    test.tlists.append(tlist)
    test.save()
