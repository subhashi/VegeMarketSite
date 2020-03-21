from django.contrib import admin
from .models import Vegetables


class VegetableAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Vegetables, VegetableAdmin)