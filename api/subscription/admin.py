from django.contrib import admin

from api.subscription.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "coach", "start_date", "end_date", "price"]
    list_filter = ["start_date", "end_date"]
    search_fields = ["user", "coach"]
    list_display_links = ["user", "coach"]
    ordering = ["-start_date"]
