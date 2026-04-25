
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)  # Allow null to start with

    def calculate_rent_price(self):
        # Define your calculation logic here
        return self.mrp * 0.1  # Example: Rent price is 10% of MRP
