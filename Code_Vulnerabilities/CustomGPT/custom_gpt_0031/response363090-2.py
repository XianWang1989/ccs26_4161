
from django.db import models, connection

class EntranceRegister(models.Model):
    authorized_requests = models.TextField()

REQUEST_TYPE_ENTRANCE = 1
REGEX_ENTRANCE = r'^{0},|,{0},|,{0}$|^{0}$'.format(REQUEST_TYPE_ENTRANCE)

# Using the custom regex function
entrance_registers = regex_search("authorized_requests", REGEX_ENTRANCE)
