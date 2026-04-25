
class CompanyProfile(models.Model):
    # Your model fields here

    def save(self, *args, **kwargs):
        super(CompanyProfile, self).save(*args, **kwargs)
