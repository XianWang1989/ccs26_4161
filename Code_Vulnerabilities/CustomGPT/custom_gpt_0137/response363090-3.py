
from django.db import connection

def entrance_query():
    REQUEST_TYPE_ENTRANCE = 1
    REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

    with connection.cursor() as cursor:
        # Make sure your REGEXP is available
        cursor.execute('CREATE FUNCTION REGEXP(pattern TEXT, search TEXT) RETURNS BOOLEAN AS $$ SELECT (search ~ pattern) $$ LANGUAGE SQL;')

        entrance_registers = EntranceRegister.objects.raw('SELECT * FROM porter_entranceregister WHERE authorized_requests REGEXP %s', [REGEX_ENTRANCE])

    return entrance_registers
