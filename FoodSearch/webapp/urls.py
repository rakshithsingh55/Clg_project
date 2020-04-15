"""URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('alogin', views.alogin, name="alogin"), 
    path('adminloginaction', views.adminlogindef, name="adminloginactiondef"),
    path('adminhome', views.adminhomedef, name="adminhome"),
    path('adminlogout', views.adminlogoutdef, name="adminlogout"),
    path('uploaddataset', views.uploaddataset, name="uploaddataset"),
    path('xlupload', views.xlupload, name="xlupload"),
    path('viewdataset', views.viewdataset, name="viewdataset"),
    path('userreg', views.userreg, name="userreg"),    
    path('signupaction', views.signupaction, name="signupaction"),
    path('slogin', views.slogin, name="slogin"),    
    path('loginaction', views.loginaction, name="loginaction"),
    path('shome', views.shome, name="shome"),
    path('slogout', views.slogout, name="slogout"),
    path('search', views.search, name="search"),
    path('searchfood', views.searchfood, name="searchfood"),
    path('viewfood/<str:name>', views.viewfood, name="viewfood"),
    path('viewfood2/<str:name>', views.viewfood2, name="viewfood2"),
    path('recommendationas', views.recommendationas, name="recommendationas"),
    
    
    

    

    
]
