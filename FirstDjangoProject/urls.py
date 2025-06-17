from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Include the URLs from the base app
    # You can add more apps here as needed
]
