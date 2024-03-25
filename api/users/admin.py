from django.contrib import admin

from api.users.models import UserProfile, CoachProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
        "phone",
        "birth_date",
        "height",
        "weight",
    ]
    list_display_links = ["id", "email"]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = ["height", "weight"]
    ordering = ["-id"]


@admin.register(CoachProfile)
class CoachProfileAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "first_name",
        "last_name",
        "phone",
        "birth_date",
        "experience",
        "rating",
        "price",
        "specialization",
    ]
    list_display_links = ["id", "email"]
    search_fields = ["first_name", "last_name", "email"]
    list_filter = ["experience", "rating"]
    ordering = ["-id"]
