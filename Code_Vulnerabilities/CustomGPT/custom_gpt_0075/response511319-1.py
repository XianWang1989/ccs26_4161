
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, editable=False)

    def save(self, *args, **kwargs):
        # Set the rent_price automatically based on mrp
        self.rent_price = self.mrp * 0.1  # Example: 10% of MRP
        super(Book, self).save(*args, **kwargs)
