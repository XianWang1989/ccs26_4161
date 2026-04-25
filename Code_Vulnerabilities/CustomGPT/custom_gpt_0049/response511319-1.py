
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate rent_price based on mrp
        self.rent_price = self.calculate_rent(self.mrp)
        super().save(*args, **kwargs)

    def calculate_rent(self, mrp):
        # Example logic for calculation (e.g., 10% of MRP)
        return mrp * 0.10  # Adjust the calculation as needed
