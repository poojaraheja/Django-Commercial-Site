from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Payal Fish Aquarium Admin"
admin.site.site_title = "Payal Fish Aquarium Portal"
admin.site.index_title = "Welcome to Payal Fish Aquarium"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]