from . import views

from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),  # Página principal del blog
]
