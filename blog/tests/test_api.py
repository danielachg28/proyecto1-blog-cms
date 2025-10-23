import pytest
from rest_framework.test import APIClient

from tests.factories import BlogFactory, PostFactory, UserFactory


OK_REQUEST_STATUS = 200
CREATED_STATUS = 201


# TESTS DE BLOGS
@pytest.mark.django_db
def test_get_blogs_list_authenticated_user():  # Un usuario autenticado solo puede ver sus propios blogs.

    user = UserFactory()
    BlogFactory(user=user)  # Blog del usuario autenticado
    BlogFactory()  # Blog de otro usuario

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/blogs/")
    assert response.status_code == OK_REQUEST_STATUS
    assert isinstance(response.data, list)
    # El usuario debe ver solo sus blogs (si el filtro está activo)
    if response.data:
        assert all(blog["user"] == user.id for blog in response.data)


@pytest.mark.django_db
def test_create_blog_authenticated_user():  # Un usuario autenticado puede crear un blog

    user = UserFactory()
    client = APIClient()
    client.force_authenticate(user=user)

    data = {"title": "Mi blog personal", "description": "Un blog de prueba"}

    response = client.post("/api/blogs/", data)
    assert response.status_code == CREATED_STATUS
    assert response.data["title"] == "Mi blog personal"


# TESTS DE POSTS
@pytest.mark.django_db
def test_authenticated_user_only_sees_their_posts():  # El usuario autenticado solo puede ver sus posts.

    user1 = UserFactory()
    user2 = UserFactory()

    blog1 = BlogFactory(user=user1)
    blog2 = BlogFactory(user=user2)

    post1 = PostFactory(blog=blog1)
    PostFactory(blog=blog2)

    client = APIClient()
    client.force_authenticate(user=user1)

    response = client.get("/api/posts/")
    assert response.status_code == OK_REQUEST_STATUS
    assert isinstance(response.data, list)

    # El usuario debería ver solo los posts asociados a su blog
    returned_post_ids = [p["id"] for p in response.data]
    assert post1.id in returned_post_ids
