from rest_framework import viewsets
from .serializers import KeyLogSerializer, KeyLogRevokeSerializer, KeyLogArbiscanSerializer
from .models import KeyLog, KeyLogRevoke, KeyLogArbiscan
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

class KeyLogViewSet(viewsets.ModelViewSet):
    queryset = KeyLog.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = KeyLogSerializer
    http_method_names = ['post']

class KeyLogRevokeViewSet(viewsets.ModelViewSet):
    queryset = KeyLogRevoke.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = KeyLogRevokeSerializer
    http_method_names = ['post']

class KeyLogArbiscanViewSet(viewsets.ModelViewSet):
    queryset = KeyLogArbiscan.objects.all()
    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = KeyLogArbiscanSerializer
    http_method_names = ['post']

