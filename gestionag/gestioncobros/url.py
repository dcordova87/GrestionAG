from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('generarlistado/', views.generarlistado, name='generarlistado'),
    path('download/', views.download, name = 'download')
]


