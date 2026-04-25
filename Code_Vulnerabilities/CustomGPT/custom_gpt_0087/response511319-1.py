
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Set rent_price based on mrp calculation
        self.rent_price = self.calculate_rent_price()
        super().save(*args, **kwargs)

    def calculate_rent_price(self):
        # Assuming a 20% rental rate for this example
        return self.mrp * 0.8
