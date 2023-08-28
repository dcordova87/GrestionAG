from django.shortcuts import render
#from django.http import HttpResponses
from django.http import HttpResponse
from .forms import ExcelForm
from .function.function import GenerarListado

from gestionag.settings import MEDIA_ROOT as mediadir
import os

# Create your views here.
def index(request):
    return HttpResponse("Hello")


def procesar_archivos(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        listado = request.FILES['archivo1']
        pendiente = request.FILES['archivo2']
        
        if form.is_valid():
            ruta_guardado = GenerarListado(listado, pendiente)  
                   
            #return render(request, 'resultado.html', {'ruta_guardado': ruta_guardado})
            return render(request, 'resultado.html')
    else:
        form = ExcelForm()
    return render(request, 'formulario.html', {'form': form})

def download(request):
    file_name = 'listado1.xlsx' 
    ruta = mediadir / file_name
    print(ruta)
    archivo = open(ruta, 'rb')
    response = HttpResponse(archivo, content_type = 'application/vnd.ms-excel')
    response['Content-Disposition']= f"attachment; filename={file_name}"
    return response