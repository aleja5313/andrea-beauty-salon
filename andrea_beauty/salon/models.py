from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre

class Cita(models.Model):

    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()
    hora = models.TimeField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Pendiente'
    )
    def __str__(self):
        return f"{self.cliente} - {self.servicio}"
    