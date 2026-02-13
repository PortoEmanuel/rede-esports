from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Postagem, Categoria

class PostagemAdmin(SummernoteModelAdmin):
    # Aqui definimos qual campo terá o editor rico
    summernote_fields = ('conteudo',)
    
    # O que vai aparecer na lista do Admin
    list_display = ('titulo', 'autor', 'categoria', 'status', 'visualizacoes', 'destaque')
    list_filter = ('status', 'categoria', 'data_publicacao', 'destaque')
    search_fields = ('titulo', 'conteudo', 'subtitulo')
    prepopulated_fields = {'slug': ('titulo',)} # Cria o slug automaticamente enquanto você digita o título
    
    # Organização do formulário no Admin para ficar profissional
    fieldsets = (
        ('Conteúdo Principal', {
            'fields': ('titulo', 'slug', 'subtitulo', 'conteudo', 'capa')
        }),
        ('Classificação e Autoria', {
            'fields': ('autor', 'categoria', 'status', 'destaque')
        }),
        ('SEO e Redes Sociais', {
            'fields': ('meta_description',),
            'description': "Configure como o artigo aparecerá no Google e WhatsApp"
        }),
        ('Métricas', {
            'fields': ('visualizacoes',),
            'classes': ('collapse',), # Deixa escondido por padrão
        }),
    )

admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Categoria)