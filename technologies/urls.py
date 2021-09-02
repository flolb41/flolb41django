from django.urls import path
from . import views

app_name = 'technologies'

urlpatterns = [
    path('', views.index, name="index"),
    path('api/GetTechs', views.api_get_techs),
]
