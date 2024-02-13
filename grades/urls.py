from django.urls import path, include

from .views import home, register, login

urlpatterns = [
    path('', home.HomeView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register.RegisterView.as_view(), name='register'),
    path('login/', login.LoginClassView.as_view(), name='login'),
]