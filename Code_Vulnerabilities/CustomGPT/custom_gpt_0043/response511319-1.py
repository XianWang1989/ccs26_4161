
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2)

    def calculate_rent_price(self):
        # Implement your calculation logic here
        # For example, let's say rent price is 10% of mrp
        return self.mrp * 0.10
