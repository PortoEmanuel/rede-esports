from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import PerfilMembro

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def gerenciar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Sempre que um Usuario for salvo, este robô é acionado.
    """
    if created:
        # Se o usuário acabou de ser criado, criamos o perfil dele
        PerfilMembro.objects.create(usuario=instance)
    else:
        # Se o usuário já existia (está sendo editado), apenas salvamos o perfil
        if hasattr(instance, 'perfil_membro'):
            instance.perfil_membro.save()