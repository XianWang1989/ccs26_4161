
from mongoengine import *

# Connect to the 'dbtest' database
connect('dbtest')


class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))


class Tlist(EmbeddedDocument):
    ref = StringField(required=True)


# Sample data
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"), ('test4', "d"),
          ('test5', "e"), ('test6', "f")]:
    test = Test()
    test.tag = i[0]
    tlist = Tlist(ref=i[1])
    test.tlists.append(tlist)
    test.save()
