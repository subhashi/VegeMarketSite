from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('fruits/', include('fruits.urls')),
    path('vegetables/', include('vegetables.urls'))
]
