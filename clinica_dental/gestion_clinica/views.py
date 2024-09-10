# gestion_clinica/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PacienteForm, CitaForm, TratamientoForm, FacturaForm, InventarioForm, HistorialClinicoForm, MedicoForm
from .models import Paciente, Cita, Tratamiento, Factura, Inventario, HistorialClinico, Medico
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
from django.template.loader import get_template

def pagina_principal(request):
    return render(request, 'base.html')

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'registrar_paciente.html', {'form': form})

def registrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm()
    return render(request, 'registrar_medico.html', {'form': form})

def programar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()
    return render(request, 'programar_cita.html', {'form': form})

def registrar_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm()
    return render(request, 'registrar_tratamiento.html', {'form': form})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'listar_pacientes.html', {'pacientes': pacientes})

def registrar_medico(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_medicos')
    else:
        form = MedicoForm()
    return render(request, 'registrar_medico.html', {'form': form})

def listar_medicos(request):
    medicos = Medico.objects.all()
    return render (request, 'listar_medicos.html', {'medicos':medicos})

def programar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()
    return render(request, 'programar_cita.html', {'form': form})

def listar_citas(request):
    citas = Cita.objects.all()
    return render(request, 'listar_citas.html', {'citas': citas})

def modificar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'modificar_cita.html', {'form': form})

def eliminar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('listar_citas')
    return render(request, 'eliminar_cita.html', {'cita': cita})    

def registrar_tratamiento(request):
    if request.method == 'POST':
        form = TratamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tratamientos')
    else:
        form = TratamientoForm()
    return render(request, 'registrar_tratamiento.html', {'form': form})

def listar_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    return render(request, 'listar_tratamientos.html', {'tratamientos': tratamientos})

def gestionar_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_facturas')
    else:
        form = FacturaForm()
    return render(request, 'gestionar_factura.html', {'form': form})

def listar_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'listar_facturas.html', {'facturas': facturas})

def generar_pdf_facturas(request):
    facturas = Factura.objects.all()
    template_path = 'gestion_clinica/facturas_pdf.html'
    context = {'facturas': facturas}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="facturas.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF: %s' % pisa_status.err)
    return response

def gestionar_inventario(request):
    if request.method == 'POST':
        form = InventarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inventario')
    else:
        form = InventarioForm()
    return render(request, 'gestionar_inventario.html', {'form': form})

def listar_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'listar_inventario.html', {'inventario': inventario})

def actualizar_historial_clinico(request):
    if request.method == 'POST':
        form = HistorialClinicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_historial_clinico')
    else:
        form = HistorialClinicoForm()
    return render(request, 'actualizar_historial_clinico.html', {'form': form})

def listar_historial_clinico(request):
    historial_clinico = HistorialClinico.objects.all()
    return render(request, 'listar_historial_clinico.html', {'historial_clinico': historial_clinico})

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def generar_pdf_pacientes(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_pacientes.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 50, "Reporte de Pacientes")

    pacientes = Paciente.objects.all()

    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 100, "ID")
    p.drawString(100, height - 100, "Nombre")
    p.drawString(200, height - 100, "Apellido")
    p.drawString(300, height - 100, "Fecha de Nacimiento")

    y = height - 120
    p.setFont("Helvetica", 12)
    for paciente in pacientes:
        p.drawString(50, y, str(paciente.id))
        p.drawString(100, y, paciente.nombre)
        p.drawString(200, y, paciente.apellido)
        p.drawString(300, y, paciente.fecha_nacimiento.strftime("%Y-%m-%d"))
        y -= 20

    p.showPage()
    p.save()

    return response

def generar_reporte_pacientes(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_pacientes.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 50, "Reporte de Pacientes")

    pacientes = Paciente.objects.all()

    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, height - 100, "ID")
    p.drawString(100, height - 100, "Nombre")
    p.drawString(200, height - 100, "Apellido")
    p.drawString(300, height - 100, "Fecha de Nacimiento")
    p.drawString(400, height - 100, "Dirección")
    p.drawString(500, height - 100, "Teléfono")
    p.drawString(600, height - 100, "Email")

    y = height - 120
    p.setFont("Helvetica", 12)

    for paciente in pacientes:
        p.drawString(50, y, str(paciente.id))
        p.drawString(100, y, paciente.nombre)
        p.drawString(200, y, paciente.apellido)
        p.drawString(300, y, paciente.fecha_nacimiento.strftime('%Y-%m-%d'))
        p.drawString(400, y, paciente.direccion)
        p.drawString(500, y, paciente.telefono)
        p.drawString(600, y, paciente.email)
        y -= 20

        if y < 50: 
            p.showPage()
            p.setFont("Helvetica", 12)
            y = height - 50

    p.showPage()
    p.save()

    return response

def generar_pdf_citas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="citas.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Lista de Citas")

    citas = Cita.objects.all()
    y = 700
    for cita in citas:
        p.drawString(100, y, f"{cita.paciente} - {cita.fecha} - {cita.hora} - {cita.descripcion}")
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def generar_pdf_tratamientos(request):
    tratamientos = Tratamiento.objects.all()
    template_path = 'gestion_clinica/tratamientos_pdf.html'
    context = {'tratamientos': tratamientos}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="tratamientos.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF: %s' % pisa_status.err)
    return response