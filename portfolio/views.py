from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio


def index(requests):
    portfolio = Portfolio.objects.all()
    return render(requests, 'portfolio/index.html', {'portfolio': portfolio})
