from rest_framework import viewsets
from .serializers import KeyLogSerializer
from .models import KeyLog
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class KeyLogViewSet(viewsets.ModelViewSet):
    queryset = KeyLog.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = KeyLogSerializer
    http_method_names = ['post']
