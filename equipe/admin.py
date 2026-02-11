from django.contrib import admin
from .models import Cargo, PerfilColaborador

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(PerfilColaborador)
class PerfilColaboradorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'exibir_cargos', 'ativo', 'data_inicio')
    list_filter = ('ativo', 'cargos')
    filter_horizontal = ('cargos',) # Cria aquela interface bonita de selecionar itens

    def exibir_cargos(self, obj):
        return ", ".join([c.nome for c in obj.cargos.all()])
    exibir_cargos.short_description = 'Cargos'