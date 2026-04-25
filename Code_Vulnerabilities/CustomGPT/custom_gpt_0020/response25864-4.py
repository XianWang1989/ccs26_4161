
# In App1's models.py
from django.db import models

class MyModel(models.Model):
    # model fields here

    class Meta:
        app_label = 'app1'

# In App2's models.py
from django.db import models

class AnotherModel(models.Model):
    # model fields here

    class Meta:
        app_label = 'app2'
