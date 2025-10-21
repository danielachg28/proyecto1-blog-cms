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
    """
    - Los usuarios autenticados pueden crear y gestionar sus propios posts.
    - Cada post se asocia automáticamente al blog del usuario autenticado.
    - Los usuarios solo ven sus propios posts (el admin puede verlos todos).
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Define qué posts se devuelven según el usuario que hace la petición.

        - Si el usuario es administrador → ve todos los posts.
        - Si está autenticado → ve solo sus posts.
        - Si no está autenticado → no ve ninguno.
        """
        user = self.request.user

        if user.is_superuser:
            # El admin puede ver todos los posts
            return Post.objects.all()
        elif user.is_authenticated:
            # Usuario normal: solo ve los posts de su blog
            return Post.objects.filter(blog__user=user)
        else:
            # Usuario no autenticado: no ve nada
            return Post.objects.none()

    def perform_create(self, serializer):
        """
        Al crear un post (POST), se ejecuta automáticamente este método.
        Asocia el post al blog del usuario autenticado antes de guardarlo.
        """
        serializer.save(blog=self.request.user.blog)


# ViewSet para Tag
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # cualquiera puede registrarse
