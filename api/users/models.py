from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name=_("user__phone"), null=True)
    birth_date = models.DateField(verbose_name=_("user__birth_date"), null=True)


class UserProfile(Profile):
    height = models.FloatField(verbose_name=_("user__height"))
    weight = models.FloatField(verbose_name=_("user__weight"))

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class CoachProfile(Profile):
    experience = models.IntegerField(verbose_name=_("coach__experience"))
    rating = models.FloatField(verbose_name=_("coach__rating"))
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("coach__price")
    )
    specialization = models.CharField(
        max_length=100, verbose_name=_("coach__specialization")
    )

    class Meta:
        verbose_name = _("Coach Profile")
        verbose_name_plural = _("Coach Profiles")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
