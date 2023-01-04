"""django_tutorial URL Configuration

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
from  django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.shopping),
    path('shopping/', views.shopping),
    # path('index/', views.index),
    path('login_homepage/', views.login_homepage),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),	
	path('adduser/', views.adduser),
    path('register/', views.register),
    # cart
    path('detail/<str:item>/<int:productid>/', views.detail),
    path('addtocart/<str:ctype>/', views.addtocart),
    path('addtocart/<str:ctype>/<int:productid>/', views.addtocart),
    path('cart/', views.cart),
    path('cartorder/', views.cartorder),
    path('cartok/', views.cartok),
    path('cartordercheck/', views.cartordercheck),
    path('keyboard/', views.keyboard),
    path('mice/', views.mice),
    path('headest/', views.headest),
]
