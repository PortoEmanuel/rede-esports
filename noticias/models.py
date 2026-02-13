from django.db import models
from django.utils.text import slugify
from equipe.models import PerfilColaborador 

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    cor_hex = models.CharField(max_length=7, default="#FF0000")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

class Postagem(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    subtitulo = models.TextField(help_text="O 'Lead' que aparece na home")
    conteudo = models.TextField() 
    
    # CONEXÃO CORRIGIDA: Apontando para PerfilColaborador
    autor = models.ForeignKey(
        PerfilColaborador, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='artigos'
    )
    
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='postagens')
    capa = models.ImageField(upload_to='noticias/capas/')
    meta_description = models.CharField(max_length=160, help_text="Descrição para o Google (SEO)")
    
    visualizacoes = models.PositiveIntegerField(default=0)
    destaque = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')
    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Postagem"
        verbose_name_plural = "Postagens"
        ordering = ['-data_publicacao']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo