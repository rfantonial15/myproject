from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KeyLogViewSet, KeyLogRevokeViewSet, KeyLogArbiscanViewSet

# Create a router and register your viewsets
router = DefaultRouter()
router.register(r'getter', KeyLogViewSet, basename='key-logs')
router.register(r'getter2', KeyLogRevokeViewSet, basename='key-logs-revoke')
router.register(r'getter3', KeyLogArbiscanViewSet, basename='key-logs-arbiscan')

# Define the URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),  # Adding the admin site URLs
    path('', include(router.urls)),  # Include the router URLs
]
