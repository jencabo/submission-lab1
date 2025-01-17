"""portalapp URL Configuration

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
from django.contrib import admin
from django.urls import path, include
import core

urlpatterns = [
    #Restaurants
    path("", include('restaurants.urls')),
    
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    #Language Toggle
    path('togglelanguage/BJL192PP<int:language_id>TTO92PP123PP/', core.views.togglelanguage, name='togglelanguage'),

    #Tenant
    path('viewcompanyprofile/BJL192PPTTO92PP123PP/', core.views.companyprofile, name='companyprofile'),
    path('editcompanyprofile/BJL192PPTTO92PP123PP/', core.views.editcompanyprofile, name='editcompanyprofile'),

    #Main
    path("", include("apps.main.urls")),             # UI Kits Html files    
]
