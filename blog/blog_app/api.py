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
class BlogViewSet(
    viewsets.ModelViewSet
):  # viewset que permite crear, leer, actualizar y eliminar modelos
    queryset = (
        Blog.objects.all()
    )  # Indica que datos manejará el viewset (en este caso, todos los blogs)
    serializer_class = BlogSerializer  # Indica el serializador que se usará para convertir los datos a JSON
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]  # Indica los permisos que se usarán para acceder a los datos


# ViewSet para Post
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Asociar el post al blog del usuario autenticado
    def perform_create(self, serializer):
        blog = self.request.user.blog  # Obtiene el blog del usuario autenticado
        serializer.save(blog=blog)  # Guarda el post con el blog del usuario autenticado


# ViewSet para Tag
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # cualquiera puede registrarse
