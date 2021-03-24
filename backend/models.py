from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from accounts.models import CustomUser
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUser


class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, related_name="purchase_user", on_delete=models.PROTECT)



