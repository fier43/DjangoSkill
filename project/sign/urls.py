from django.urls import path
from .views import IndexView, LoginFormView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
]
