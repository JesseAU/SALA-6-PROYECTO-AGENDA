from django.db import models

PRIORIDAD_CHOICES = [
    ('alta', 'Alta'),
    ('media', 'Media'),
    ('baja', 'Baja'),
]

ESTADO_CHOICES = [
    ('pendiente', 'Pendiente'),
    ('en_proceso', 'En proceso'),
    ('completo', 'Completo'),
]

class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_limite = models.DateField()
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES)

    def __str__(self):
        return f"{self.descripcion} - {self.estado}"
