from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TrainingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.training"
    verbose_name = _("Trainings")
