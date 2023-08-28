from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('formulario/', views.procesar_archivos, name='procesar_archivos'),
    path('download/', views.download, name = 'download')
]


