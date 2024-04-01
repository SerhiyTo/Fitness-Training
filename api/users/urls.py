from django.urls import path

from api.users.views import UserProfileObtainToken, CoachProfileObtainToken, UserProfileView, CoachProfileView

urlpatterns = [
    path("token/user/", UserProfileObtainToken.as_view(), name="user_login"),
    path("token/coach/", CoachProfileObtainToken.as_view(), name="coach_login"),
    path("register/user/", UserProfileView.as_view(), name="user_registration"),
    path("register/coach/", CoachProfileView.as_view(), name="coach_registration"),
]
