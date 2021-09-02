from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Technologies


def index(requests):
    technologies = Technologies.objects.all().order_by()
    return render(requests, 'technologies/index.html', {'technologies': technologies})


def api_get_techs(requests):
    technologies = Technologies.objects.all()
    json = serializers.serialize("json", technologies)
    return HttpResponse(json)