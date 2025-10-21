# Librerías para importar/exportar datos
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# TinyMCE: editor visual de texto
from tinymce.widgets import TinyMCE

# Importa los modelos (las clases que representan las tablas del blog)
from .models import Blog, Post, Tag

# Importa el panel de administración de Django
from django.contrib import admin

# Importa la base de campos de Django (para personalizar campos del formulario)
from django.db import models


# ------------------------------------------------------
# 3.3 Configurar django-import-export para los Posts
# ------------------------------------------------------
# Este recurso define qué campos se pueden exportar o importar
class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created_at", "updated_at", "blog")


# ------------------------------------------------------
# 3.2 y 3.4 Configurar el panel de administración de Post
# ------------------------------------------------------
@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    # Vincula el recurso de import/export
    resource_class = PostResource

    # Qué columnas mostrar en la lista del admin
    list_display = ("title", "blog", "created_at", "updated_at")

    # Qué filtros laterales mostrar
    list_filter = ("created_at", "tags")

    # Campos por los que se puede buscar
    search_fields = ("title", "content")

    # Usa TinyMCE para el campo de texto "content"
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE(attrs={"cols": 80, "rows": 20})},
    }

    # ------------------------------------------------------
    # 3.5 Permisos: mostrar solo los posts del usuario actual
    # ------------------------------------------------------
    def get_queryset(self, request):
        # Obtiene todos los posts
        queryset = super().get_queryset(request)
        # Si es superusuario, ve todos los posts
        if request.user.is_superuser:
            return queryset
        # Si no, solo ve los de su propio blog
        return queryset.filter(blog__user=request.user)

    # ------------------------------------------------------
    # 3.5 Asignar el blog automáticamente al crear un post
    # ------------------------------------------------------
    def save_model(self, request, obj, form, change):  # noqa: PLR6301
        # Si el post es nuevo (no tiene id todavía)
        if not obj.pk:
            # Asigna el blog del usuario conectado
            obj.blog = request.user.blog
        obj.save()


# ------------------------------------------------------
# Configuración sencilla para los otros modelos
# ------------------------------------------------------


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "user")  # Mostrar título y dueño del blog


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# ------------------------------------------------------
# Registrar los modelos en el panel de administración
# ------------------------------------------------------
# Esto es lo que hace que aparezcan en el panel de Django
