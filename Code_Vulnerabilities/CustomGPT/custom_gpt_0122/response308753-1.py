
# Example setup
from gluon import current

db = current.db
db.define_table('example', Field('name'))
