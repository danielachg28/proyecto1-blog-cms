from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import AllowAny

from .models import Blog, Post, Tag
from .serializers import (
    BlogSerializer,
    PostSerializer,
    RegisterSerializer,
    TagSerializer,
)

from django.contrib.auth.models import User


# ViewSet para Blog
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ViewSet para Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Asociar el post al blog del usuario autenticado
    def perform_create(self, serializer):
        blog = self.request.user.blog
        serializer.save(blog=blog)


# ViewSet para Tag
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # cualquiera puede registrarse
    serializer_class = RegisterSerializer
