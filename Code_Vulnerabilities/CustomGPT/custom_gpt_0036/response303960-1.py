
from mongoengine import *

# Connect to the MongoDB database named 'dbtest'
connect('dbtest')

# Define the embedded document
class Tlist(EmbeddedDocument):
    ref = StringField(required=True)

# Define the main document
class Test(Document):
    tag = StringField(required=True)
    tlists = ListField(EmbeddedDocumentField('Tlist'))

# Sample data to be stored in the database
for i in [('test1', "a"), ('test2', "b"), ('test3', "c"),
          ('test1', "a"), ('test2', "b"), ('test3', "c")]:

    # Create an instance of Test
    test = Test()
    test.tag = i[0]

    # Create an instance of Tlist and append it to the test instance
    tlist = Tlist()
    tlist.ref = i[1]
    test.tlists.append(tlist)

    # Save the instance to the database
    test.save()
