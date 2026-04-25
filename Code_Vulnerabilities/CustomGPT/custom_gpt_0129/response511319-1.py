
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the rent_price based on some logic applied to mrp.
        # For example, let's assume rent_price is 20% of mrp.
        if self.mrp:
            self.rent_price = self.mrp * 0.2
        super().save(*args, **kwargs)
