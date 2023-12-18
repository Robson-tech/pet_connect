from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include("petconnect.urls"), name='petconnect'),
    path('admin/', admin.site.urls),
]
