
# app1/models.py
from django.db import models

class Model1(models.Model):
    # fields here
    class Meta:
        app_label = 'app1'

# app2/models.py
from django.db import models

class Model2(models.Model):
    # fields here
    class Meta:
        app_label = 'app2'
