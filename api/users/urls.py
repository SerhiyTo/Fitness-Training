from django.urls import path

from api.users.views import BaserProfileObtainToken, CoachListView, SubscriptionUserListView, UserRegisterView


urlpatterns = [
    path("token/", BaserProfileObtainToken.as_view(), name="user_login"),
    path("register/", UserRegisterView.as_view(), name="user_registration"),
    path("coaches/", CoachListView.as_view(), name="coach_list"),
    path("subscriptions/", SubscriptionUserListView.as_view(), name="user_subscriptions"),
]
