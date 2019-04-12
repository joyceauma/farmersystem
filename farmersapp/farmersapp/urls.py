"""farmersapp URL Configuration

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
from rest_framework import routers                    
from accounts import views 
#from .views import index

router = routers.DefaultRouter()
router.register('officer/', views.OfficerView, 'officer')
router.register('farmer/', views.FarmerView, 'farmer')
router.register('session/', views.SessionView, 'session')
router.register('report/', views.ReportView, 'report') 

urlpatterns = [
path('admin/', admin.site.urls), 
path('api', include(router.urls)),
path('', views.index, name='index'),
#path('', include('accounts.urls')),
#path('login', views.login, name='login'),
]

