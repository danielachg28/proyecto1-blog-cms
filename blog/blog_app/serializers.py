from rest_framework import serializers

from .models import Blog, Post, Tag

from django.contrib.auth.models import User


# Serializador para Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


# Serializador para Post
class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)  # Mostrar tags dentro del post
    blog = serializers.StringRelatedField(read_only=True)  # Mostrar nombre del blog

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "updated_at", "blog", "tags"]


# Serializador para Blog
class BlogSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)  # Mostrar posts del blog

    class Meta:
        model = Blog
        fields = ["id", "title", "description", "user", "posts"]
        read_only_fields = [
            "user"
        ]  # esto hace que no sea obligatorio enviarlo al crear un blog


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):  # noqa: PLR6301
        user = User.objects.create_user(  # Para guardar la contraseña cifrada
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user
