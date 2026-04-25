
import re
from django.db import models
from django.db.models import Q
from django.db.models import Func

# Custom function to use regex
class RegexMatch(Func):
    function = 'REGEXP'

def get_entrance_registers(request_type):
    regex_pattern = r'^{0},|,{0},|,{0}$|^{0}$'.format(request_type)

    if models.Dao.objects.db.vendor == 'sqlite':
        # For SQLite: fetch all and filter in Python
        entrance_registers = EntranceRegister.objects.all()
        return [
            register for register in entrance_registers
            if re.search(regex_pattern, register.authorized_requests)
        ]
    else:
        # For PostgreSQL (or other supporting DB)
        return EntranceRegister.objects.filter(authorized_requests__regex=regex_pattern)

# Usage
entrance_registers = get_entrance_registers(1)
