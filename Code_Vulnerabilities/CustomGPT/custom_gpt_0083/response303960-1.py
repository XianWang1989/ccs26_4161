
from mongoengine import connect, Document, StringField, ListField, EmbeddedDocumentField, EmbeddedDocument

# Connect to the database
connect('dbtest')

# Define your Embedded Document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define your main Document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))

# Sample data to populate the database
for i in [('test1', "a"), ('test2', "b"), ('test3', "c")]:
    test = Test(tag=i[0])
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
