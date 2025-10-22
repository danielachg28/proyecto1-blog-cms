import pytest
from rest_framework.test import APIClient

from tests.factories import BlogFactory


OK_REQUEST_STATUS = 200


@pytest.mark.django_db
def test_get_blogs_list():  # Prueba que el endpoint /api/blogs/ devuelva la lista de blogs correctamente
    BlogFactory.create_batch(2)  # Crea 2 blogs de prueba en la base de datos
    client = APIClient()  # Cliente de pruebas para hacer peticiones HTTP

    response = client.get("/api/blogs/")  # Hace una petición GET
    assert response.status_code == OK_REQUEST_STATUS  # La respuesta debe ser exitosa
    assert isinstance(response.data, list)  # Debe devolver una lista
