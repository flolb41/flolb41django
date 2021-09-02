from django.contrib import admin
from .models import Technologies


class TechnologiesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'logo', 'description', 'frontend', 'backend')
    search_fields = ['nom']


# Register your models here.
admin.site.register(Technologies, TechnologiesAdmin)
