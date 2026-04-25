
import re
from django.db import connection
from django.db.models import Func

def regex_func(expr, item):
    return re.match(expr, item) is not None

def register_regex_function():
    with connection.cursor() as cursor:
        cursor.execute("CREATE FUNCTION REGEXP(expr TEXT, item TEXT) RETURNS BOOLEAN AS 'SELECT CASE WHEN ? IS NULL OR ? IS NULL THEN NULL ELSE ? END' " 
                       "LANGUAGE SQL", (expr, item, regex_func))

class Regexp(Func):
    function = 'REGEXP'

class YourAppConfig(AppConfig):
    name = 'your_app_name'

    def ready(self):
        register_regex_function()

# In your view or wherever you need to perform the query
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.filter(
    authorized_requests__regex=REGEX_ENTRANCE
)
