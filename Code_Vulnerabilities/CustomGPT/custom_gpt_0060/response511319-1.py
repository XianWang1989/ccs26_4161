
from django.db import models

class Book(models.Model):
    mrp = models.DecimalField(max_digits=9, decimal_places=2)
    rent_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Optionally calculate rent_price during save if you want to ensure it stays synced
        self.rent_price = self.calculate_rent_price()
        super().save(*args, **kwargs)

    def calculate_rent_price(self):
        # Example calculation: rent_price is 70% of mrp
        return self.mrp * 0.7 if self.mrp else 0.00
