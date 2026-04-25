
from django.db import models

class EntranceRegister(models.Model):
    authorized_requests = models.TextField()

# Query with custom regex
REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

entrance_registers = EntranceRegister.objects.extra(
    where=["regexp(%s, authorized_requests)" % REGEX_ENTRANCE], 
    params=[REGEX_ENTRANCE]
)
