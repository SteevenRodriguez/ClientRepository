from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'

class ClientFormConfig(AppConfig):
    name = 'RegistrRegistro de Ventas'