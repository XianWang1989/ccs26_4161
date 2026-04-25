
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def calculate_rent_price(self):
        # Example calculation (25% of MRP)
        return round(self.mrp * 0.25, 2)
