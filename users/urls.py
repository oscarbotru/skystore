from django.urls import path

from users.apps import UsersConfig
from users.views import SigninView, RegisterView, ResetView, ConfirmView, LogoutView, DashboardView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', SigninView.as_view(), name='login'),
    path('confirm/<key>/', ConfirmView.as_view(), name='confirm'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
