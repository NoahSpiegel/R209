from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.read),
    path('<int:pk>/update', views.update, name="garage_update"),
]