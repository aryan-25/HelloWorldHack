"""Volunteer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('accounts/', include('allauth.urls')),
    path('volunteer/', login_required(views.Home.as_view()), name='home'),
    path('places/', login_required(views.Places.as_view()), name='places'),
    path('opportunity/', login_required(views.Opportunity.as_view()), name='opportunity'),
    path('volunteer/request/', login_required(views.MakeRequest.as_view()), name='request'),
    path('volunteer/thankyou', views.thankyou, name='thankyou'),
]