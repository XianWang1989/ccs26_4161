
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2)

    def save(self, *args, **kwargs):
        # Autoset rent_price based on mrp
        self.rent_price = self.calculate_rent_price()
        super().save(*args, **kwargs)

    def calculate_rent_price(self):
        # Example calculation (e.g., 10% of MRP)
        return self.mrp * 0.1
