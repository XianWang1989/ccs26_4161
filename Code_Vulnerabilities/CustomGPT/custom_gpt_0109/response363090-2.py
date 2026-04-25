
import re
from django.db import connection

def regex_func(pattern, value):
    return re.match(pattern, value) is not None

def create_regex_function():
    connection.cursor().execute("CREATE FUNCTION REGEXP(pattern TEXT, value TEXT) RETURNS INTEGER AS $$ "
                                 "BEGIN "
                                 "RETURN CASE WHEN value REGEXP pattern THEN 1 ELSE 0 END; "
                                 "END; $$ LANGUAGE plpgsql;")

create_regex_function()
