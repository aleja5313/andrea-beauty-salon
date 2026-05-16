from django.contrib import admin
from .models import Cliente, Servicio, Cita

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'telefono',
        'email'
    )

    search_fields = (
        'nombre',
        'telefono',
        'email'
    )

    ordering = (
        'nombre',
    )

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'precio',
        'duracion'
    )

    search_fields = (
        'nombre',
    )

    list_filter = (
        'precio',
    )

    ordering = (
        'nombre',
    )

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):

    list_display = (
        'cliente',
        'servicio',
        'fecha',
        'hora',
        'estado'
    )

    search_fields = (
        'cliente__nombre',
        'servicio__nombre'
    )

    list_filter = (
        'estado',
        'fecha'
    )

    ordering = (
        '-fecha',
    )