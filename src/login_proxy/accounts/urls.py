from django.urls import path
from django.contrib.auth import views as auth_views
from login_proxy.accounts import views

app_name = "Account"

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('accounts/profile/', views.profile),
]
