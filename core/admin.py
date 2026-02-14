from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    # 1. Campos que aparecem na lista (para você ver quem tem e-mail e quem não tem)
    list_display = ('username', 'email', 'is_equipe', 'is_membro', 'is_staff')
    list_filter = ('is_equipe', 'is_membro', 'is_staff')

    # 2. Campos para a tela de ADICIONAR novo usuário (Evita o erro de e-mail vazio)
    # Aqui forçamos o e-mail a aparecer logo no cadastro inicial
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Pessoais', {
            'fields': ('email', 'first_name', 'last_name'),
        }),
        ('Controle de Acesso Rede Esports', {
            'fields': ('is_equipe', 'is_membro'),
        }),
    )

    # 3. Campos para a tela de EDIÇÃO (Quando o usuário já existe)
    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        new_fieldsets = list(fieldsets)
        
        # Evita duplicar se você salvar o arquivo e o Django recarregar
        if not any('Controle de Acesso Rede Esports' in str(fs) for fs in new_fieldsets):
            new_fieldsets.append(
                ('Controle de Acesso Rede Esports', {
                    'fields': ('is_equipe', 'is_membro'),
                })
            )
        return new_fieldsets