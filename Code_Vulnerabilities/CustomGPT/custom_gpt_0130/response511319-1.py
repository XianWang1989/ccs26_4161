
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.rent_price is None:
            self.rent_price = self.calculate_rent_price()
        super().save(*args, **kwargs)

    def calculate_rent_price(self):
        # Example calculation: 10% of MRP
        return round(self.mrp * 0.1, 2)
