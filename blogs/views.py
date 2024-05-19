from rest_framework import viewsets
from rest_framework import permissions
from blogs.models import Blogs
from blogs.serializers import BlogsSerializer


class BlogsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

    def get_queryset(self):
        return Blogs.objects.all()
