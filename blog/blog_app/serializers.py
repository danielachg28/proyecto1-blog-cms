from rest_framework import serializers

from .models import Blog, Post, Tag


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
