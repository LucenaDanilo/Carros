from django.contrib import admin
from cars.models import Car, Brand

# Register your models here.
# crudzinho vai rolar aqui ein

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'year', 'value')
    search_fields = ('model', 'brand__name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)