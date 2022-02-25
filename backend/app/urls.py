from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)


urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('get-user/', views.getUser, name="get-user"),
    path('get-files/', views.getFiles, name="get-files"),
    #path('get-file/<str:pk>', views.getFileById, name="get-file"),
    path('upload-file/', views.uploadFile, name="upload-file"),
    #path('get-file-data/<str:pk>', views.getFileData, name="get-file-data"),
    path('get-files-data/', views.getFilesData, name="get-files-data"),
    path('get-user-history/', views.getUserHistory, name="get-user-history"),
]