import factory

from blog_app.models import Blog, Post

from django.contrib.auth.models import User


# Usuario de prueba
class UserFactory(
    factory.django.DjangoModelFactory
):  # Cada vez que se llama a UserFactory() se crea un nuevo usuario en la base de datos de test
    class Meta:
        model = User

    username = factory.Faker("user_name")  # Genera un nombre de usuario aleatorio
    email = factory.Faker("email")  # Genera un correo aleatorio
    password = factory.PostGenerationMethodCall("set_password", "testpass123")
    # Usa el método set_password para que la contraseña quede cifrada correctamente


# Blog de prueba
class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.Faker("sentence", nb_words=3)  # Título falso
    description = factory.Faker("text")  # Descripción falsa
    user = factory.SubFactory(
        UserFactory
    )  # Asocia automáticamente un usuario creado por UserFactory


# Post de prueba
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("sentence")  # Título aleatorio
    content = factory.Faker("paragraph")  # Contenido falso
    blog = factory.SubFactory(BlogFactory)  # Asocia automáticamente un blog
