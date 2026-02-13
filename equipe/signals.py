from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Usuario  # Verifique se o seu modelo de user está aqui
from .models import PerfilColaborador

@receiver(post_save, sender=Usuario)
def criar_perfil_automatico(sender, instance, created, **kwargs):
    if created:
        # Se um novo usuário foi criado, cria um perfil para ele
        PerfilColaborador.objects.create(usuario=instance)

@receiver(post_save, sender=Usuario)
def salvar_perfil_automatico(sender, instance, **kwargs):
    # Garante que se o usuário for atualizado, o perfil também seja salvo
    if hasattr(instance, 'perfil_equipe'):
        instance.perfil_equipe.save()