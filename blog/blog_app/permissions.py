from rest_framework import permissions


# --- Helpers ---
def is_authenticated(user):
    return user and user.is_authenticated


def is_superuser(user):
    return user.is_superuser


def is_owner(user, obj):
    """
    Verifica si el usuario es propietario del objeto
    """
    if hasattr(obj, "user"):
        return obj.user == user
    if hasattr(obj, "blog"):
        return obj.blog.user == user
    return False


def is_owner_of_any_post(user, obj):
    """
    Verifica si el usuario es dueño de al menos un post asociado (para Tags).
    """
    if hasattr(obj, "posts"):
        return obj.posts.filter(blog__user=user).exists()
    return False


# --- Permissions ---
class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permiso que permite acceso a:
    - Superusuarios
    - Propietarios del objeto (obj.user)
    """

    def has_permission(self, request, view):  # noqa: PLR6301
        return is_authenticated(request.user)

    def has_object_permission(self, request, view, obj):  # noqa: PLR6301
        user = request.user
        return is_superuser(user) or is_owner(user, obj)


class IsBlogOwnerOrAdmin(permissions.BasePermission):
    """
    Permiso para recursos relacionados con blogs:
    - Posts: obj.blog.user
    - Tags: al menos un post asociado
    """

    def has_permission(self, request, view):  # noqa: PLR6301
        return is_authenticated(request.user)

    def has_object_permission(self, request, view, obj):  # noqa: PLR6301
        user = request.user
        if is_superuser(user):
            return True
        if hasattr(obj, "blog"):
            return is_owner(user, obj)
        if hasattr(obj, "posts"):
            return is_owner_of_any_post(user, obj)
        return False


class IsAuthenticatedOrReadOnlyOwner(permissions.BasePermission):
    """
    - Usuarios no autenticados: sin acceso
    - Usuarios autenticados: acceso solo a sus propios recursos
    - Superusuarios: acceso total
    """

    def has_permission(self, request, view):  # noqa: PLR6301
        return is_authenticated(request.user)

    def has_object_permission(self, request, view, obj):  # noqa: PLR6301
        user = request.user
        if is_superuser(user):
            return True
        return is_owner(user, obj)
