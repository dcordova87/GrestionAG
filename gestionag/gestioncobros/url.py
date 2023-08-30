from django.urls import path
from . import views
from django.views import defaults as default_views

urlpatterns = [
    path('', views.index, name = "index"),
    path('generarlistado/', views.generarlistado, name='generarlistado'),
    path('download/', views.download_files, name = 'download'),
    path('*', views.page_not_found, name = 'page_not_found'),
    path('download/selected/', views.download_selected_files, name='download_selected'),
]

handler404 = default_views.page_not_found
