
from mongoengine import *

connect('dbtest')


class Tlist(EmbeddedDocument):
    ref = StringField(required=True)


class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField(Tlist))


# Example data for testing
data = [('test1', "a"), ('test2', "b"), ('test3', "c"),
        ('test1', "a"), ('test2', "b"), ('test3', "c")]

for i in data:
    test = Test()
    test.tag = i[0]
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)
    test.save()
