from django.urls import path
from django_proj.urls import account_app_name
from django.contrib.auth import views as auth_views
from accounts import views as acv

app_name = account_app_name

urlpatterns = [
    path('', acv.home, name='home'),
    path('/update', acv.UserUpdateView.as_view(), name='update'),
    path('/profile/', acv.profile, name='profile'),
    path('/signup', acv.signup, name='signup'),
    path('/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('/logout', auth_views.LogoutView.as_view(), name='logout'),
 
]
