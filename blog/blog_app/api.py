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
    queryset = Blog.objects.none()  # vacío por defecto
    serializer_class = BlogSerializer  # Indica el serializador que se usará para convertir los datos a JSON
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]  # Indica los permisos que se usarán para acceder a los datos

    # define qué elementos se mostrarán según el usuario logueado
    def get_queryset(self):
        """
        Si el usuario es superuser, ve todos los blogs.
        Si es un usuario normal, solo ve su propio blog.
        """
        user = self.request.user  # Usuario autenticado (o anónimo si no está logueado)
        # Si el usuario no está autenticado, devuelve un queryset vacío
        if not user.is_authenticated:
            return Blog.objects.none()

        # Si es superusuario, puede ver todos los blogs
        if user.is_superuser:
            return Blog.objects.all()

        # Usuario normal: solo ve su propio blog
        return Blog.objects.filter(user=user)

    # se ejecuta automáticamente cuando se crea un nuevo blog (POST
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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

        # No autenticado → no ve nada
        if not user.is_authenticated:
            return Post.objects.none()

        # Superusuario → ve todo
        if user.is_superuser:
            return Post.objects.all()

        # Usuario normal → solo sus posts
        return Post.objects.filter(blog__user=user)

    def perform_create(self, serializer):
        """
        Si el usuario no tiene blog, se le crea automáticamente.
        Cada nuevo post se asocia al blog del usuario.
        """
        user = self.request.user
        blog, created = Blog.objects.get_or_create(
            user=user,
            defaults={
                "title": f"Blog de {user.username}",
                "description": "Blog creado automáticamente.",
            },
        )
        serializer.save(blog=blog)


# ViewSet para Tag
class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            return Tag.objects.none()

        if user.is_superuser:
            return Tag.objects.all()

        # Solo tags asociados a posts del blog del usuario
        return Tag.objects.filter(posts__blog__user=user).distinct()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # cualquiera puede registrarse
