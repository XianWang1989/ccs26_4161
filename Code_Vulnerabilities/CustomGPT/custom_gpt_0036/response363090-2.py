
import sqlite3
import re

def regex_function(pattern, string):
    return 1 if re.search(pattern, string) else 0

# Inside your settings or where you set up your database connection
from django.db.backends.signals import connection_created

def add_regex_function(sender, connection, **kwargs):
    connection.create_function("REGEXP", 2, regex_function)

# Connect the signal
from django.db import models
from django.dispatch import receiver

@receiver(connection_created)
def connection_listener(sender, connection, **kwargs):
    add_regex_function(sender, connection)

# Then you can use the REGEXP operator as follows:
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)
entrance_registers = EntranceRegister.objects.raw(
    'SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP ?', (REGEX_ENTRANCE,)
)
