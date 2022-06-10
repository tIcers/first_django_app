from django.urls import path
from . import views


# first_app/
urlpatterns = [
    path('', views.simple_view),
]
