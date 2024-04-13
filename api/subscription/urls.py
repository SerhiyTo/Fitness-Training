from django.urls import path

from api.subscription.views import SubscriptionView, SubscriptionListView

urlpatterns = [
    path("subscribe/", SubscriptionView.as_view(), name="subscribe"),
    path("subscriptions/", SubscriptionListView.as_view(), name="subscriptions"),
]
