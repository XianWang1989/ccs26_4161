
from django.db import models

class Book(models.Model):  
    mrp        = models.DecimalField(max_digits=9, decimal_places=2)  
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)  

    def __str__(self):
        return f"Book MRP: {self.mrp}, Rent Price: {self.rent_price}"
