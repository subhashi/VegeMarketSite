from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home),
    path('fruits/', include('fruits.urls')),
    path('vegetables/', include('vegetables.urls'))
]
