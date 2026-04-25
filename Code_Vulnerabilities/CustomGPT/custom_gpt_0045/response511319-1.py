
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Optionally, you can include logic for calculating rent_price based on mrp here
        if self.mrp:
            self.rent_price = self.mrp * 0.1  # Example calculation: 10% of the MRP
        super().save(*args, **kwargs)
