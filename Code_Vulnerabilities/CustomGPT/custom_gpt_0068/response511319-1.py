
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def calculate_rent_price(self):
        # Define your calculation logic here. For example, let's say rent_price is 10% of mrp
        return self.mrp * 0.10 if self.mrp else 0
