
import re
from django.db.models import Q

class EntranceRegisterQuerySet(models.QuerySet):
    def filter_by_regex(self, request_type):
        regex = r'^{0},|,{0},|,{0}$|^{0}$'.format(request_type)
        return self.filter(Q(authorized_requests__icontains=request_type))

# Usage
entrance_registers = EntranceRegister.objects.all().filter_by_regex(REQUEST_TYPE_ENTRANCE)
