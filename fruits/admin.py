from django.contrib import admin
from .models import Fruit


class FruitsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


admin.site.register(Fruit, FruitsAdmin)