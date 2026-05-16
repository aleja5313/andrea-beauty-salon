from django.urls import path
from . import views

app_name = 'salon'

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path(
        'clientes/',
        views.ClienteListView.as_view(),
        name='clientes'
    ),
    path(
        'clientes/nuevo/',
        views.ClienteCreateView.as_view(),
        name='cliente_create'
    ),
    path(
        'clientes/<int:pk>/editar/',
        views.ClienteUpdateView.as_view(),
        name='cliente_update'
    ),
    path(
        'clientes/<int:pk>/eliminar/',
        views.ClienteDeleteView.as_view(),
        name='cliente_delete'
    ),
    path(
    'servicios/',
    views.ServicioListView.as_view(),
    name='servicios'
),

    path(
    'servicios/nuevo/',
    views.ServicioCreateView.as_view(),
    name='servicio_create'
),

    path(
    'servicios/<int:pk>/editar/',
    views.ServicioUpdateView.as_view(),
    name='servicio_update'
),

    path(
    'servicios/<int:pk>/eliminar/',
    views.ServicioDeleteView.as_view(),
    name='servicio_delete'
),
    path(
    'citas/',
    views.CitaListView.as_view(),
    name='citas'
),

    path(
    'citas/nueva/',
    views.CitaCreateView.as_view(),
    name='cita_create'
),

    path(
    'citas/<int:pk>/editar/',
    views.CitaUpdateView.as_view(),
    name='cita_update'
),

    path(
    'citas/<int:pk>/eliminar/',
    views.CitaDeleteView.as_view(),
    name='cita_delete'
),
]