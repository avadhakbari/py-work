from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_product/', views.upload_product, name='upload_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
]