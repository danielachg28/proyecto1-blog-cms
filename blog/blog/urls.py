"""
URL configuration for blog project.

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

from rest_framework import routers

from blog_app.api import BlogViewSet, PostViewSet, RegisterView, TagViewSet

from django.contrib import admin
from django.urls import include, path


# Crear router automáticamente
router = routers.DefaultRouter()
router.register(r"blogs", BlogViewSet)
router.register(r"posts", PostViewSet)
router.register(r"tags", TagViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),  # Panel de administración
    path("tinymce/", include("tinymce.urls")),  # Rutas de TinyMCE
    path("api/", include(router.urls)),  # API REST
    path("api-auth/", include("rest_framework.urls")),  # Login para DRF
    path("api/register/", RegisterView.as_view(), name="register"),  # registro
    path("", include("blog_app.urls")),  # Rutas normales del blog
]
