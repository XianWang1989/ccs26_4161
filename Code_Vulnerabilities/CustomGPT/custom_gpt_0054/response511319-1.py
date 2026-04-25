
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Optionally enforce calculation logic on model save
        if self.mrp:
            self.rent_price = self.calculate_rent_price(self.mrp)
        super().save(*args, **kwargs)

    def calculate_rent_price(self, mrp):
        # Define your business logic for rent price calculation
        return mrp * 0.1  # Example: rent price is 10% of MRP
