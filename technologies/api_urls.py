from django.urls import path
from . import views

app_name = 'technologies_api'

urlpatterns = [
    path('GetTechs', views.api_get_techs),
]