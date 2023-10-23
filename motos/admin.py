from django.contrib import admin
from motos.models import Motos, Brand

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MotosAdmin(admin.ModelAdmin):
    list_display = ('model', 'factory_year', 'year', 'value')
    search_fields = ('model', 'brand__name',)

admin.site.register(Motos, MotosAdmin)
admin.site.register(Brand, BrandAdmin)
