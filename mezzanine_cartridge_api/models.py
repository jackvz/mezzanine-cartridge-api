from django.db import models

# Model for in-memory Django/Mezzanine settings
class SystemSetting(models.Model):
    name = models.CharField()
    value = models.CharField()
    class Meta:
        managed = False
