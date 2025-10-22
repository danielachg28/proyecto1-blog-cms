import pytest

from tests.factories import BlogFactory, PostFactory, UserFactory


@pytest.mark.django_db
def test_user_factory_creates_valid_user():
    """
    Verifica que la UserFactory crea un usuario válido y funcional.
    """
    user = UserFactory()
    assert user.username is not None  # Se genera un nombre de usuario
    assert user.password != " "  # Tiene una contraseña cifrada
    assert user.is_active  # El usuario está activo por defecto


# pytest.mark.django_db permite acceder a la base de datos de pruebas
@pytest.mark.django_db
def test_blog_is_created_with_user():  # Crea un blog y verifica que tenga un usuario asociado.

    blog = BlogFactory()  # Usa la factory para crear un blog
    assert blog.user is not None  # Comprueba que el blog tiene usuario


@pytest.mark.django_db
def test_post_is_linked_to_blog():  # Crea un post y verifica que esté asociado a un blog.

    post = PostFactory()
    assert post.blog is not None  # El post debe tener un blog asociado
