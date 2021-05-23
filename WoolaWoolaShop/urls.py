"""WoolaWoolaShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import earrings.views

urlpatterns = [
    path('', earrings.views.home, name='home'),
    path('story/', earrings.views.story, name='story'),
    path('collections/', earrings.views.collections, name='collections'),
    path('restricted/', earrings.views.restricted, name='restricted'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('earrings/', include('earrings.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls'))
]
