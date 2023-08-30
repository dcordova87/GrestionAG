from django.shortcuts import render
from django.http import HttpResponse
from .forms import ExcelForm
from .function.function import GenerarListado

from gestionag.settings import MEDIA_ROOT as mediadir
import os
import zipfile

# Create your views here.
def index(request):
    return render(request, 'gestioncobros/index.html')


def generarlistado(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST, request.FILES)
        listado = request.FILES['archivo1']
        pendiente = request.FILES['archivo2']
        
        if form.is_valid():
            nombre_archivo = form.cleaned_data['nombre_archivo'] # ojo el form solo tiene el metodo cleaned_data si es valido
            ruta_guardado = GenerarListado(listado, pendiente, nombre_archivo)
            nombre_archivo = nombre_archivo + '.xlsx'

            ##voy a poner el codigo de la vista anterior par aver si funciona
            archivo = open(ruta_guardado, 'rb')
            response = HttpResponse(archivo, content_type = 'application/vnd.ms-excel')
            response['Content-Disposition']= f"attachment; filename={nombre_archivo}"
            return response
            ##aqui termina el codigo de la otra vista
              
            #request.session['nombre_archivo'] = nombre_archivo      
            #return render(request, 'resultado.html', {'ruta_guardado': ruta_guardado})
            #return render(request, 'resultado.html', {'ruta_guardado':ruta_guardado, 'nombre_archivo':nombre_archivo})
    else:
        form = ExcelForm()
    return render(request, 'gestioncobros/formlistado.html', {'form': form})

# def download(request):
#     #file_name = 'listado1.xlsx'
#     #print(nombre_archivo)
#     file_name = file_name1 + '.xlsx'
#     print(file_name)

#     #file_name = self.kwargs['nombre_archivo'] 
#     #file_name = file_name + '.xlsx'
#     ruta = mediadir / file_name
#     print(ruta)
#     archivo = open(ruta, 'rb')
#     response = HttpResponse(archivo, content_type = 'application/vnd.ms-excel')
#     response['Content-Disposition']= f"attachment; filename={file_name}"
#     return response


def download_files(request):
    # Define the directory path
    #directory_path = os.path.join(settings.MEDIA_ROOT, 'mediadir')
    directory_path = mediadir

    # Get all the files in the directory
    files = os.listdir(directory_path)

    # Render the template with the list of files
    return render(request, 'gestioncobros/download.html', {'files': files})

def download_selected_files(request):
    selected_files = request.POST.getlist('selected_files')

    # Create a zip file containing the selected files
    zip_filename = 'selected_files.zip'
    zip_filepath = os.path.join(mediadir, zip_filename)
    with zipfile.ZipFile(zip_filepath, 'w') as zipf:
        for file in selected_files:
            file_path = os.path.join(mediadir, file)
            zipf.write(file_path, file)

    # Open the zip file and read its content
    with open(zip_filepath, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="selected_files.zip"'

    # Delete the zip file
    os.remove(zip_filepath)

    return response

def page_not_found(request):
    return render(request, '404.html')