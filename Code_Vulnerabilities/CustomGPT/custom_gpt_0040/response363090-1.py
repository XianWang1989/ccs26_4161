
import re
from django.db import connection
from django.db.models import Q

# Step 1: Create a custom regex function
def regex_filter(value, pattern):
    return bool(re.match(pattern, value))

# Step 2: Register the regex function with the SQLite connection
def create_regex_function():
    connection.execute("CREATE TEMP FUNCTION REGEXP(pattern TEXT, value TEXT) RETURNS INTEGER AS $$
        SELECT CASE WHEN value REGEXP pattern THEN 1 ELSE 0 END;
    $$ LANGUAGE SQL;")

# Step 3: Use regex in your query
def get_entrance_registers(request_type):
    REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(request_type)

    # Register the regex function
    create_regex_function()

    # Fetch matching records
    entrance_registers = EntranceRegister.objects.filter(
        Q(authorized_requests__regex=REGEX_ENTRANCE)
    )
    return entrance_registers

# Usage
REQUEST_TYPE_ENTRANCE = 1
results = get_entrance_registers(REQUEST_TYPE_ENTRANCE)
