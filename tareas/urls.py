from django.urls import path
from . import views

urlpatterns = [
    path('', views.TareaListView.as_view(), name='tarea-list'),
    path('crear/', views.TareaCreateView.as_view(), name='tarea-crear'),
    path('editar/<int:pk>/', views.TareaUpdateView.as_view(), name='tarea-editar'),
    path('borrar/<int:pk>/', views.TareaDeleteView.as_view(), name='tarea-borrar'),
]
