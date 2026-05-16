from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy

from .models import Cita, Cliente, Servicio

from .forms import (
    ClienteForm,
    ServicioForm,
    CitaForm
)

def dashboard(request):

    total_clientes = Cliente.objects.count()

    total_servicios = Servicio.objects.count()

    total_citas = Cita.objects.count()

    citas_pendientes = Cita.objects.filter(
        estado='Pendiente'
    ).count()

    ultimas_citas = Cita.objects.order_by(
        '-fecha'
    )[:5]

    context = {

        'total_clientes': total_clientes,

        'total_servicios': total_servicios,

        'total_citas': total_citas,

        'citas_pendientes': citas_pendientes,

        'ultimas_citas': ultimas_citas,
    }

    return render(
        request,
        'salon/dashboard.html',
        context
    )

class ClienteListView(ListView):

    model = Cliente

    template_name = 'salon/clientes/list.html'

    context_object_name = 'clientes'


class ClienteCreateView(CreateView):

    model = Cliente

    form_class = ClienteForm

    template_name = 'salon/clientes/create.html'

    success_url = reverse_lazy('salon:clientes')
    
    def form_valid(self, form):

        messages.success(
            self.request,
            'Cliente creado correctamente.'
        )

        return super().form_valid(form)
    
class ClienteUpdateView(UpdateView):

    model = Cliente

    form_class = ClienteForm

    template_name = 'salon/clientes/update.html'

    success_url = reverse_lazy('salon:clientes')

    def form_valid(self, form):

        messages.success(
            self.request,
            'Cliente actualizado correctamente.'
        )

        return super().form_valid(form)
    
class ClienteDeleteView(DeleteView):

    model = Cliente

    template_name = 'salon/clientes/delete.html'

    success_url = reverse_lazy('salon:clientes')


class ServicioListView(ListView):

    model = Servicio

    template_name = 'salon/servicios/list.html'

    context_object_name = 'servicios'


class ServicioCreateView(CreateView):

    model = Servicio

    form_class = ServicioForm

    template_name = 'salon/servicios/create.html'

    success_url = reverse_lazy('salon:servicios')


class ServicioUpdateView(UpdateView):

    model = Servicio

    form_class = ServicioForm

    template_name = 'salon/servicios/update.html'

    success_url = reverse_lazy('salon:servicios')


class ServicioDeleteView(DeleteView):

    model = Servicio

    template_name = 'salon/servicios/delete.html'

    success_url = reverse_lazy('salon:servicios')


class CitaListView(ListView):

    model = Cita

    template_name = 'salon/citas/list.html'

    context_object_name = 'citas'


class CitaCreateView(CreateView):

    model = Cita

    form_class = CitaForm

    template_name = 'salon/citas/create.html'

    success_url = reverse_lazy('salon:citas')

    def form_valid(self, form):

        messages.success(
            self.request,
            'Cita creada correctamente.'
        )

        return super().form_valid(form)
    
class CitaUpdateView(UpdateView):

    model = Cita

    form_class = CitaForm

    template_name = 'salon/citas/update.html'

    success_url = reverse_lazy('salon:citas')

    def form_valid(self, form):

        messages.success(
            self.request,
            'Cita actualizada correctamente.'
        )

        return super().form_valid(form)
    
class CitaDeleteView(DeleteView):

    model = Cita

    template_name = 'salon/citas/delete.html'

    success_url = reverse_lazy('salon:citas')