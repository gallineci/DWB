from django.contrib import admin
from veiculo.models import Veiculo

class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'ano', )
# Register your models here.