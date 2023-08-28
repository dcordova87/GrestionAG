from django import forms

class ExcelForm(forms.Form):
    archivo1 = forms.FileField()
    archivo2 = forms.FileField()