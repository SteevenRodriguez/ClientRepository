from django.contrib import admin
from .models import Patient, Doctor, Product, Register

"""
Inlines
"""

"""
Register models
"""
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    fields = ('cedula', 'nombre', 'edad','sexo','procedencia','origen', 'derivacion', 'tratamiento')
    list_display = ('nombre', 'edad', 'sexo', 'derivacion', 'tratamiento',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fields = ('nombre',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('nombre', 'precio',)
    list_display = ('nombre', 'precio',)

@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    fields = ('fecha','paciente',)
  #  inlines = [PatientInLine]
    #readonly_fields = ('paciente__nombre', 'paciente__edad',)
    def get_paciente(self,obj):
        return obj.paciente.nombre
    def get_paciente_edad(self,obj):
        return obj.paciente.edad 
    def get_paciente_sexo(self,obj):
        return obj.paciente.sexo
    def get_paciente_derivacion(self,obj):
        return obj.paciente.derivacion
    def get_paciente_tratamiento(self,obj):
        return obj.paciente.tratamiento
    def get_paciente_money(self,obj):
        return obj.paciente.tratamiento.precio
    list_display = ('fecha', 'get_paciente', 'get_paciente_edad','get_paciente_sexo','get_paciente_tratamiento','get_paciente_money')
