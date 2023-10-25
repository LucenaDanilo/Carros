from django.contrib import admin
from motos.models import Motos, Brand_Motos

# Register your models here.
class BrandMotosAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class MotosAdmin(admin.ModelAdmin):
    list_display = ('model', 'factory_year', 'year', 'value')
    search_fields = ('model', 'brand__name',)

admin.site.register(Brand_Motos, BrandMotosAdmin)
admin.site.register(Motos, MotosAdmin)
