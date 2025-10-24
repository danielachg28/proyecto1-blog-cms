from django.contrib.auth.models import User
from django.db import models


# 2.1 Blog con relación 1:1 con User
class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="blog")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


# 2.2 Post con campos básicos
class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # fecha de actualización

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]  # 2.4 Metadatos: orden descendente por fecha


# 2.3 Tag y relación M:N con Post
class Tag(models.Model):
    name = models.CharField(max_length=50)
    posts = models.ManyToManyField("Post", related_name="tags", blank=True)

    def __str__(self):
        return self.name
