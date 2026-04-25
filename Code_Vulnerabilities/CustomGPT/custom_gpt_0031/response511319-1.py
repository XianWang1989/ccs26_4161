
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Auto-calculate rent_price based on mrp before saving
        if self.mrp:
            self.rent_price = self.mrp * 0.1  # Example calculation
        super().save(*args, **kwargs)
