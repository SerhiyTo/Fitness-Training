from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(AbstractUser):
    email = models.EmailField(unique=True, verbose_name=_("User email"))
    phone = models.CharField(max_length=20, null=True, verbose_name=_("User phone"))
    birth_date = models.DateField(null=True, verbose_name=_("User birthdate"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class UserProfile(Profile):
    height = models.FloatField(verbose_name=_("User height"))
    weight = models.FloatField(verbose_name=_("User weight"))

    class Meta:
        verbose_name = _("User Profile")
        verbose_name_plural = _("User Profiles")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class CoachActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class CoachProfile(Profile):
    experience = models.IntegerField(verbose_name=_("Coach experience"))
    rating = models.FloatField(verbose_name=_("Coach rating"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Coach price"))
    specialization = models.CharField(max_length=100, verbose_name=_("Coach specialization"))

    objects = models.Manager()
    active = CoachActiveManager()

    class Meta:
        verbose_name = _("Coach Profile")
        verbose_name_plural = _("Coach Profiles")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
