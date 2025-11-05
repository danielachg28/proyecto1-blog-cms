# Create your views here.
from django.http import HttpResponse


# Vista creada como ejemplo para evitar el error 404
def home(request):
    return HttpResponse("Blog")
