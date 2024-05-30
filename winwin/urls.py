from django.contrib import admin
from django.urls import path

from winwin.views.auth_view import UserLoginView, UserRegistrationView
from winwin.views.media_live_view import create_channel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('channels/', create_channel, name='create_channel'),

]
