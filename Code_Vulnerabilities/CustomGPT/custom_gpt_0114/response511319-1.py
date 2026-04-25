
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate the rent price based on mrp, e.g., 10% of mrp
        self.rent_price = self.mrp * 0.1
        super().save(*args, **kwargs)
