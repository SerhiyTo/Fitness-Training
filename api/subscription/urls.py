from django.urls import path

from api.subscription.views import SubscriptionView


urlpatterns = [
    path("", SubscriptionView.as_view(), name="subscriptions"),
    path("<int:pk>/", SubscriptionView.as_view(), name="subscription-detail"),
]
