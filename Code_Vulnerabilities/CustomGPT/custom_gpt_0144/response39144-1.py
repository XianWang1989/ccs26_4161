class CompanyProfile(models.Model):
    # your fields here

    def save(self, *args, **kwargs):
        # custom logic (if any)
        super().save(*args, **kwargs)
