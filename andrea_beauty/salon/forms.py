from django import forms

from .models import Cliente, Servicio, Cita


class ClienteForm(forms.ModelForm):

    class Meta:

        model = Cliente

        fields = [
            'nombre',
            'telefono',
            'email'
        ]

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'telefono': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

        }

    def clean_telefono(self):

        telefono = self.cleaned_data.get('telefono')

        if not telefono.isdigit():

            raise forms.ValidationError(
                'El teléfono solo debe contener números.'
            )

        if len(telefono) < 10:

            raise forms.ValidationError(
                'El teléfono debe tener mínimo 10 dígitos.'
            )

        return telefono


class ServicioForm(forms.ModelForm):

    class Meta:

        model = Servicio

        fields = '__all__'

        widgets = {

            'nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'descripcion': forms.Textarea(attrs={
                'class': 'form-control'
            }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'duracion': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

        }

    def clean_precio(self):

        precio = self.cleaned_data.get('precio')

        if precio <= 0:

            raise forms.ValidationError(
                'El precio debe ser mayor a cero.'
            )

        return precio

    def clean_duracion(self):

        duracion = self.cleaned_data.get('duracion')

        if duracion <= 0:

            raise forms.ValidationError(
                'La duración debe ser mayor a cero.'
            )

        return duracion


class CitaForm(forms.ModelForm):

    class Meta:

        model = Cita

        fields = '__all__'

        widgets = {

            'cliente': forms.Select(attrs={
                'class': 'form-select'
            }),

            'servicio': forms.Select(attrs={
                'class': 'form-select'
            }),

            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'hora': forms.TimeInput(attrs={
                'class': 'form-control'
            }),

            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),

        }
        
        
def clean(self):

    cleaned_data = super().clean()

    fecha = cleaned_data.get('fecha')

    hora = cleaned_data.get('hora')

    cita_existente = Cita.objects.filter(
        fecha=fecha,
        hora=hora
    )


    if self.instance.pk:

        cita_existente = cita_existente.exclude(
            pk=self.instance.pk
        )

    if cita_existente.exists():

        raise forms.ValidationError(
            'Ya existe una cita programada para esa fecha y hora.'
        )

    return cleaned_data

    def clean_hora(self):

        hora = self.cleaned_data.get('hora')

        if hora:

            if hora.hour < 8 or hora.hour > 19:

                raise forms.ValidationError(
                    'Las citas solo pueden programarse entre 8 AM y 7 PM.'
                )

        return hora