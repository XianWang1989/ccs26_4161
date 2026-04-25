
import re
from django.db import connection
from yourapp.models import EntranceRegister

def create_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION regexp(pattern, value) RETURNS INTEGER AS $$ "
                       "BEGIN "
                       "RETURN ($2 ~ $1); "
                       "END; $$ LANGUAGE plpgsql;")

def get_entrance_registers(request_type):
    REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(request_type)
    create_regex_function()

    entrance_registers = EntranceRegister.objects.raw(
        'SELECT * FROM porter_entranceregister WHERE regexp(%s, authorized_requests)',
        [REGEX_ENTRANCE]
    )

    return entrance_registers

# Example usage
REQUEST_TYPE_ENTRANCE = 1
entrance_registers = get_entrance_registers(REQUEST_TYPE_ENTRANCE)
