from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from admin_totals.admin import ModelAdminTotals
from .models import Patient, Doctor, Product, Record
from import_export import resources
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.db.models import Sum, Avg
from django.db.models.functions import Coalesce
"""
Inlines
"""

"""
Register models
"""
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    fields = ('cedula', 'nombre', 'edad','sexo','procedencia','origen', 'derivacion','diagnostico',)
    list_display = ('nombre', 'edad', 'sexo', 'derivacion','diagnostico' ,)
    list_filter = ('edad', 'sexo','diagnostico')
    search_fields = ('cedula', 'nombre','derivacion__nombre' )

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    fields = ('nombre','especialidad')
    list_display = ('nombre','especialidad')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('tratamiento', 'precio',)
    list_display = ('tratamiento', 'precio',)

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
        fields = ('fecha','paciente__nombre','paciente__edad','paciente__sexo',
        'product__tratamiento','paciente__derivacion__nombre')

@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin):
    resource_class = RecordResource
    #fields = ('fecha','paciente','product')
    def get_paciente(self,obj):
        return obj.paciente.nombre
    def get_paciente_edad(self,obj):
        return obj.paciente.edad 
    def get_paciente_sexo(self,obj):
        return obj.paciente.sexo
    def get_paciente_derivacion(self,obj):
        return obj.paciente.derivacion
    def get_paciente_tratamiento(self,obj):
        return obj.product.tratamiento
    def get_paciente_money(self,obj):
        return obj.product.precio

    get_paciente.short_description = "Paciente"
    get_paciente_edad.short_description = "Edad"
    get_paciente_sexo.short_description = "Sexo"
    get_paciente_derivacion.short_description = "Derivado"
    get_paciente_tratamiento.short_description = "Tratamiento"
    get_paciente_money.short_description = "Precio"
    
    list_display = ('fecha', 'paciente', 'get_paciente_edad','get_paciente_sexo','get_paciente_derivacion','get_paciente_tratamiento','get_paciente_money')
    list_filter = (('fecha',DateRangeFilter),'paciente__edad','paciente__sexo','product__tratamiento')
    search_fields = ('paciente__nombre','paciente__edad','paciente__sexo','product__tratamiento')