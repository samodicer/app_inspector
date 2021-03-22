from django.urls import path
from . import views


urlpatterns = [
    path('get-files/', views.getFiles, name="get-files"),
    path('get-file/<str:pk>', views.getFileById, name="get-file"),
    path('upload-file/', views.uploadFile, name="upload-file"),
    path('get-file-data/<str:pk>', views.getFileData, name="get-file-data"),
]