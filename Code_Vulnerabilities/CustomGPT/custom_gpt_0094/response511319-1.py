
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def calculate_rent_price(self):
        return self.mrp * 0.1  # Example calculation, adjust as needed
