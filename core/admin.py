from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # Campos que aparecem na lista
    list_display = ('username', 'email', 'is_equipe', 'is_membro', 'is_staff')
    list_filter = ('is_equipe', 'is_membro', 'is_staff')


    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        new_fieldsets = list(fieldsets) # Transformamos em lista para o VS Code aceitar
        
        
        new_fieldsets.append(
            ('Controle de Acesso Rede Esports', {
                'fields': ('is_equipe', 'is_membro'),
            })
        )
        return new_fieldsets