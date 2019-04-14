from django.db import models
from django.conf import settings as django_settings
from enum import Enum

from drf_braces.serializers.form_serializer import FormSerializer
from enumfields import EnumIntegerField

# Conditionally include Cartridge models, if the Cartridge package is installed
try:
    from cartridge.shop.forms import OrderForm
except:
    pass

# Model for in-memory Django/Mezzanine settings
class SystemSetting(models.Model):
    name = models.TextField()
    value = models.TextField()
    class Meta:
        managed = False

# Conditionally include Cartridge models, if the Cartridge package is installed
try:
    # Form for Cartridge orders
    class CheckoutForm(OrderForm):
        class OneStepType(Enum):
            CHECKOUT = 1
        class TwoStepsType(Enum):
            ADDRESS = 1
            PAYMENT = 2
        class OneStepWithConfirmationType(Enum):
            CHECKOUT = 1
            CONFIRMATION = 2
        class TwoStepsWithConfirmationType(Enum):
            ADDRESS = 1
            PAYMENT = 2
            CONFIRMATION = 3
    step = EnumIntegerField(enum=OneStepType, default=OneStepType.UNRESOLVED)
    if django_settings.SHOP_CHECKOUT_STEPS_SPLIT and django_settings.SHOP_PAYMENT_STEP_ENABLED:
        step = EnumIntegerField(enum=TwoStepsType, default=TwoStepsType.UNRESOLVED)
    if django_settings.SHOP_CHECKOUT_STEPS_CONFIRMATION:
        step = EnumIntegerField(enum=OneStepWithConfirmationType, default=OneStepWithConfirmationType.UNRESOLVED)
        if django_settings.SHOP_CHECKOUT_STEPS_SPLIT and django_settings.SHOP_PAYMENT_STEP_ENABLED:
            step = EnumIntegerField(enum=TwoStepsWithConfirmationType, default=TwoStepsWithConfirmationType.UNRESOLVED)

except:
    pass
