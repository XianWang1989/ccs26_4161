
class CompanyProfile(models.Model):
    # Your fields here, e.g., name = models.CharField(max_length=100)

    def save(self, force_insert=False, force_update=False):
        super(CompanyProfile, self).save(force_insert, force_update)
