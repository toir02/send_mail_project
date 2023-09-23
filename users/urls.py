from django.urls import path

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', verification_user, name='verification'),
    path('success_verification/', success_verification, name='success_verification'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
