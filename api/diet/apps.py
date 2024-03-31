from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DietConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.diet"
    verbose_name = _("Diets")
