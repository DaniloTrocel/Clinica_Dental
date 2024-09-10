# gestion_clinica/forms.py
from django import forms
from django.db import models
from .models import Paciente, Medico, Cita, Tratamiento, Factura, Inventario, HistorialClinico

class PacienteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )

    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )

    class Meta:
        model = Medico
        fields = '__all__'

class CitaForm(forms.ModelForm):
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )

    class Meta:
        model = Cita
        fields = '__all__'

class TratamientoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )

    class Meta:
        model = Tratamiento
        fields = '__all__'

class FacturaForm(forms.ModelForm):
    fecha_emision = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y'],
        required=True
    )

    class Meta:
        model = Factura
        fields = ['total', 'fecha_emision', 'paciente', 'tratamiento', 'descripcion']

class InventarioForm(forms.ModelForm):
    fecha_ingreso = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )

    class Meta:
        model = Inventario
        fields = '__all__'

class HistorialClinicoForm(forms.ModelForm):
    fecha_consulta = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y']
    )

    class Meta:
        model = HistorialClinico
        fields = '__all__'