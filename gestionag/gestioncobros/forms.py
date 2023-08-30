from django import forms

from django import forms

class ExcelForm(forms.Form):
    archivo1 = forms.FileField(label='Seleccione el listado', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    archivo2 = forms.FileField(label='Seleccione el pendiente', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    nombre_archivo = forms.CharField(label='Nombre del archivo', widget=forms.TextInput(attrs={'class': 'form-control'}))

class ExcelForm1(forms.Form):
    archivo1 = forms.FileField(label='Seleccione el listado')
    archivo2 = forms.FileField(label='Seleccione el pendiente')
    nombre_archivo = forms.CharField(label='Nombre del archivo')