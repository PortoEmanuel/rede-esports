from django.db import models
from django.conf import settings

class PerfilMembro(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='perfil_membro'
    )
    
    # --- Identidade Visual ---
    nickname = models.CharField('Nickname/ID', max_length=50, blank=True)
    avatar = models.ImageField('Foto de Perfil', upload_to='avatares/', blank=True, null=True)
    cor_perfil = models.CharField('Cor de Destaque', max_length=7, default='#ff0000')
    
    # --- Social & Gamificação ---
    bio = models.TextField('Biografia', max_length=500, blank=True)
    twitter_user = models.CharField('Twitter/X', max_length=30, blank=True)
    instagram_user = models.CharField('Instagram', max_length=30, blank=True)
    discord_id = models.CharField('Discord ID', max_length=50, blank=True)
    
    # --- Preferências (Ouro para o seu Marketing) ---
    jogos_favoritos = models.CharField(
        'Jogos de Interesse', 
        max_length=255, 
        help_text="Ex: LoL, CS2, Valorant",
        blank=True
    )
    time_coracao = models.CharField('Time Favorito', max_length=100, blank=True)
    
    # --- Dados de Lead/Engajamento ---
    receber_noticias = models.BooleanField('Newsletter', default=True)
    pontos_engajamento = models.PositiveIntegerField(default=0) # Para gamificação futura
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Perfil do Membro'
        verbose_name_plural = 'Perfis da Comunidade'

    def __str__(self):
        return str(self.nickname or self.usuario.username)