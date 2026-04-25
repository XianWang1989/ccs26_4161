
import django
from django.db import connection

def custom_conn():
    connection.connection = create_connection()

CUSTOM_SQLITE_CONNECTION = True
