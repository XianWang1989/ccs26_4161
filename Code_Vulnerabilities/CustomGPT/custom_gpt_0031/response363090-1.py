
import re
from django.db import connection

def regex_search(field_name, regex):
    with connection.cursor() as cursor:
        return cursor.execute(f"SELECT * FROM porter_entranceregister WHERE {field_name} REGEXP ?", [regex]).fetchall()
