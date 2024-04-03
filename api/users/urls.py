from django.urls import path

from api.users.views import BaserProfileObtainToken, UserRegisterView

urlpatterns = [
    path("token/", BaserProfileObtainToken.as_view(), name="user_login"),
    path("register/", UserRegisterView.as_view(), name="user_registration"),
]
