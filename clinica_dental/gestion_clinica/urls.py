# gestion_clinica/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('registrar_paciente/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('registrar_medico/', views.registrar_medico, name='registrar_medico'),
    path('listar_medicos/', views.listar_medicos, name='listar_medicos'),
    path('programar_cita/', views.programar_cita, name='programar_cita'),
    path('citas/', views.listar_citas, name='listar_citas'),
    path('modificar_cita/<int:id>/', views.modificar_cita, name='modificar_cita'),
    path('eliminar_cita/<int:id>/', views.eliminar_cita, name='eliminar_cita'),
    path('registrar_tratamiento/', views.registrar_tratamiento, name='registrar_tratamiento'),
    path('tratamientos/', views.listar_tratamientos, name='listar_tratamientos'),
    path('gestionar_factura/', views.gestionar_factura, name='gestionar_factura'),
    path('listar_facturas/', views.listar_facturas, name='listar_facturas'),
    path('generar_pdf_facturas/', views.generar_pdf_facturas, name='generar_pdf_facturas'),
    path('gestionar_inventario/', views.gestionar_inventario, name='gestionar_inventario'),
    path('inventario/', views.listar_inventario, name='listar_inventario'),
    path('actualizar_historial_clinico/', views.actualizar_historial_clinico, name='actualizar_historial_clinico'),
    path('historial_clinico/', views.listar_historial_clinico, name='listar_historial_clinico'),
    path('generar_pdf_pacientes/', views.generar_pdf_pacientes, name='generar_pdf_pacientes'),
    path('generar_pdf_citas/', views.generar_pdf_citas, name='generar_pdf_citas'),
    path('generar_pdf_tratamientos/', views.generar_pdf_tratamientos, name='generar_pdf_tratamientos'),
    ]