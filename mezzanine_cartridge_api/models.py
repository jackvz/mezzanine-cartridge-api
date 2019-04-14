from django.db import models

# Model for in-memory Django/Mezzanine settings
class SystemSetting(models.Model):
    name = models.TextField()
    value = models.TextField()
    class Meta:
        managed = False
