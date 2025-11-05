import graphene  # pyright: ignore[reportMissingImports]
from graphene_django import DjangoObjectType  # pyright: ignore[reportMissingImports]

from blog_app.models import Blog, Post, Tag
from blog_app.serializers import BlogSerializer, PostSerializer, TagSerializer


# Tipos para las consultas (Queries)
class BlogType(DjangoObjectType):
    class Meta:
        model = Blog
        fields = "__all__"


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "updated_at", "blog", "tags")


class TagType(DjangoObjectType):
    class Meta:
        model = Tag
        fields = ("id", "name", "posts")


# Consultas (queries)
class Query(graphene.ObjectType):
    all_blogs = graphene.List(BlogType)
    all_posts = graphene.List(PostType)
    all_tags = graphene.List(TagType)

    def resolve_all_blogs(self, info):  # noqa: ARG002, PLR6301
        return Blog.objects.all()

    def resolve_all_posts(self, info):  # noqa: ARG002, PLR6301
        return Post.objects.all()

    def resolve_all_tags(self, info):  # noqa: ARG002, PLR6301
        return Tag.objects.all()


# Mutations reutilizando los serializers DRF
# === Mutations basadas en Serializers DRF (manual, sin librería externa) ===
class CreateBlog(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=False)

    blog = graphene.Field(BlogType)
    errors = graphene.List(graphene.String)

    def mutate(self, info, title, description=None):  # noqa: PLR6301
        data = {"title": title, "description": description}
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            blog = serializer.save()
            return CreateBlog(blog=blog, errors=[])
        errors = [
            f"{field}: {', '.join(msgs)}" for field, msgs in serializer.errors.items()
        ]
        return CreateBlog(blog=None, errors=errors)


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        blog_id = graphene.Int(required=True)
        tag_ids = graphene.List(graphene.Int)

    post = graphene.Field(PostType)
    errors = graphene.List(graphene.String)

    def mutate(self, info, title, content, blog_id, tag_ids=None):  # noqa: PLR6301
        data = {
            "title": title,
            "content": content,
            "blog": blog_id,
            "tags": tag_ids or [],
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return CreatePost(post=post, errors=[])
        errors = [
            f"{field}: {', '.join(msgs)}" for field, msgs in serializer.errors.items()
        ]
        return CreatePost(post=None, errors=errors)


class CreateTag(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    tag = graphene.Field(TagType)
    errors = graphene.List(graphene.String)

    def mutate(self, info, name):  # noqa: PLR6301
        serializer = TagSerializer(data={"name": name})
        if serializer.is_valid():
            tag = serializer.save()
            return CreateTag(tag=tag, errors=[])
        errors = [
            f"{field}: {', '.join(msgs)}" for field, msgs in serializer.errors.items()
        ]
        return CreateTag(tag=None, errors=errors)


# === Mutation Root ===
class Mutation(graphene.ObjectType):
    create_blog = CreateBlog.Field()
    create_post = CreatePost.Field()
    create_tag = CreateTag.Field()


# === Schema principal ===
schema = graphene.Schema(query=Query, mutation=Mutation)
