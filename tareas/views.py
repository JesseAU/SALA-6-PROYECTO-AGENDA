from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tarea

class TareaListView(ListView):
    model = Tarea
    template_name = 'tareas/tarea_list.html'

class TareaCreateView(CreateView):
    model = Tarea
    fields = ['descripcion', 'fecha_limite', 'prioridad', 'estado']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tarea-list')

class TareaUpdateView(UpdateView):
    model = Tarea
    fields = ['descripcion', 'fecha_limite', 'prioridad', 'estado']
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tarea-list')

class TareaDeleteView(DeleteView):
    model = Tarea
    template_name = 'tareas/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea-list')
