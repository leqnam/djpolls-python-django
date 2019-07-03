"""django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from djpolls import views
from djpolls.apps import DjpollsConfig
from accounts.apps import AccountsConfig

from django.conf.urls import url
from django.contrib import admin # authentication system
from django.contrib.auth import views as auth_views # authentication system

djpolls_app_name = DjpollsConfig.name # follow here: https://stackoverflow.com/a/56054638/5027340
account_app_name = AccountsConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path(djpolls_app_name, include('djpolls.urls', namespace='djpolls_app_name')),
    path(account_app_name, include('accounts.urls', namespace='account_app_name')),
    
    
    path('', include('djpolls.urls')),
    # or
    # path('', views.home),
]
