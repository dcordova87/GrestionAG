from django import forms

class ExcelForm(forms.Form):
    archivo1 = forms.FileField(label='Seleccione el listado')
    archivo2 = forms.FileField(label='Seleccione el pendiente')
    nombre_archivo = forms.CharField(label='Nombre del archivo')