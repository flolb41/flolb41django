from django.contrib import admin
from .models import Portfolio


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('nom', 'image', 'description', 'lien')
    search_fields = ['nom']


# Register your models here.
admin.site.register(Portfolio, PortfolioAdmin)
