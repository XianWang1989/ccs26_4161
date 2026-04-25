class CompanyProfile(models.Model):
    # fields...

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        super(CompanyProfile, self).save(force_insert=force_insert, force_update=force_update, *args, **kwargs)
