
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppTerapia/index.html',
        context=contexto,
    )
    return http_response

#usar el puerto 8888 para el comando python manage.py runserver 8888

