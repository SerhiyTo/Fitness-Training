from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.users.models import UserProfile, CoachProfile


class ActiveSubscriptionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end_date__gte=timezone.now())


class Subscription(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="subscription_user")
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE, related_name="subscription_coach")
    start_date = models.DateField(verbose_name=_("subscription__start_date"))
    end_date = models.DateField(verbose_name=_("subscription__end_date"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("subscription__price"))

    active = ActiveSubscriptionManager()
    objects = models.Manager()

    class Meta:
        verbose_name = _("Subscription")
        verbose_name_plural = _("Subscriptions")

    def __str__(self):
        return f"{self.user} - {self.coach}"
