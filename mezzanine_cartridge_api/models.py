from django.db import models

# Model for in-memory Django/Mezzanine settings
class SystemSetting():
    name = models.CharField()
    value = models.CharField()
    class Meta:
        ordering = ('name',)
