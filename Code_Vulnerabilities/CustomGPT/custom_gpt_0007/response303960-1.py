
from mongoengine import *

connect('dbtest')


class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))


class Tlist(EmbeddedDocument):
    ref = StringField(required=True)


# Example Data Insertion
data = [('test1', "a"), ('test2', "b"), ('test3', "c")]

for item in data:
    test = Test()
    test.tag = item[0]
    tlist = Tlist()
    tlist.ref = item[1]
    test.tlists.append(tlist)
    test.save()
