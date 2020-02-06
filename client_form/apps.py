from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

class ClientFormConfig(AppConfig):
    name = 'client_form'
    verbose_name = 'Registro de Ventas'