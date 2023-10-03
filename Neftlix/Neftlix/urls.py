"""
URL configuration for Neftlix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from drf_yasg import openapi
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view

schema_view=get_schema_view(
    openapi.Info(
        title="Cinema Application Rest API",
        default_version="v1",
        description="Swagger docs for REST API",
        contact=openapi.Contact("Karimov Ixtiyor <karimovixtiyor98@gmail.com"),

    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cinema.urls')),
    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0),name='swagger-docs'),
    path('redocs/',schema_view.with_ui('redoc',cache_timeout=0),name='redoc-docs')
]
