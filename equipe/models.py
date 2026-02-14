from django.db import models
from django.conf import settings

class Cargo(models.Model):
    nome = models.CharField('Nome do Cargo', max_length=100, unique=True)
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    def __str__(self):
        return str(self.nome)

class PerfilColaborador(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_equipe')
    cargos = models.ManyToManyField(Cargo, related_name='colaboradores', blank=True)
    data_inicio = models.DateField('Data de Início', auto_now_add=True)
    ativo = models.BooleanField('Ativo na Equipe', default=True)

    class Meta:
        verbose_name = 'Perfil do Colaborador'
        verbose_name_plural = 'Perfis da Equipe'

    def __str__(self):
        return f"{self.usuario.username} - Colaborador"

class FotoGaleria(models.Model):
    titulo = models.CharField('Título da Imagem', max_length=200)
    imagem = models.ImageField(upload_to='galeria/%Y/%m/')
    fotografo = models.ForeignKey(PerfilColaborador, on_delete=models.SET_NULL, null=True, related_name='fotos')
    data_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto da Galeria'
        verbose_name_plural = 'Galeria de Fotos'

    def __str__(self):
        return self.titulo