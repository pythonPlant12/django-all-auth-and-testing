from rest_framework import viewsets

from authors.models import Authors
from authors.serializers import AuthorsSerializer

# Create your views here.


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
