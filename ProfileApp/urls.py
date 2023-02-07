"""djangoProj182 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ProfileApp import views

urlpatterns = [
    path('Profile', views.Profile, name="Profile"),
    path('Education', views.Education, name="Education"),
    path('Attention', views.Attention, name="Attention"),
    path('Career', views.Career, name="Career"),
    path('RoleModel', views.RoleModel, name="RoleModel"),
    path('ShowMyData', views.ShowMyData, name="ShowMyData"),
    path('listProduct', views.listProduct, name='listProduct'),
    path('inputProduct', views.inputProduct, name='inputProduct'),
    path('showGoodsList', views.showGoodsList, name='showGoodsList'),
]
