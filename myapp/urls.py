from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeyLogViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'getter', KeyLogViewSet, basename='key-logs')

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Adding the admin site URLs
    path('', include(router.urls)),  # Include the router URLs
]
