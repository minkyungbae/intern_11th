from django.urls import path
from accounts.views import signup_views, login_views

app_name = "accounts"
urlpatterns = [
    path("signup/", signup_views.SignupAPIView.as_view(), name="signup"), # 회원 가입
]
