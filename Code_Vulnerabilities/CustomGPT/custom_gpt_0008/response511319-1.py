
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically calculate rent_price from mrp before saving
        if self.mrp:
            self.rent_price = self.mrp * 0.1  # Example calculation: 10% of MRP
        super().save(*args, **kwargs)
