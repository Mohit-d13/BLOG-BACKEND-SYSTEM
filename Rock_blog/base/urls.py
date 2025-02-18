from django.urls import path
from .views import index, signup

from django.contrib.auth import views
from .forms import LoginForm

app_name = 'base'

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='base/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]