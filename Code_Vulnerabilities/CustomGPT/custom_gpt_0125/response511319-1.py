
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate the rent_price based on mrp, for example, 10% of the MRP
        self.rent_price = self.mrp * 0.10  
        super(Book, self).save(*args, **kwargs)
