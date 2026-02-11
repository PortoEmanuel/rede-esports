from django.contrib import admin
from .models import PerfilMembro

@admin.register(PerfilMembro)
class PerfilMembroAdmin(admin.ModelAdmin):
    # O que aparece na tabela principal
    list_display = ('get_username', 'nickname', 'receber_noticias', 'cor_perfil')
    
    # Filtros para você achar rápido quem quer receber marketing
    list_filter = ('receber_noticias',)
    
    # Busca por nome de usuário ou nickname
    search_fields = ('usuario__username', 'nickname')
    
    # Organização dentro da edição do perfil
    fieldsets = (
        ('Identificação', {
            'fields': ('usuario', 'nickname', 'avatar')
        }),
        ('Personalização', {
            'fields': ('cor_perfil', 'bio')
        }),
        ('Marketing & Leads', {
            'fields': ('receber_noticias',),
            'description': 'Controle se o torcedor está na sua lista de e-mail.'
        }),
    )

    def get_username(self, obj):
        return obj.usuario.username
    get_username.short_description = 'Usuário'