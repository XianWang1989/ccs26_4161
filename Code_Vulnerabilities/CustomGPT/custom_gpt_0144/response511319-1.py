from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2)

    def calculate_rent_price(self):
        # You can replace this with your own formula for rent price calculation
        return self.mrp * 0.1  # Example: rent price is 10% of mrp
