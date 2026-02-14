from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import PerfilColaborador

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def gerenciar_perfil_usuario(sender, instance, created, **kwargs):
    """
    Cria um PerfilColaborador automaticamente quando um novo Usuario é criado
    se o usuário for marcado como parte da equipe.
    """
    if created:
        PerfilColaborador.objects.create(usuario=instance)
    else:
        # Se o perfil já existir, apenas garante que ele seja salvo
        if hasattr(instance, 'perfil_equipe'):
            instance.perfil_equipe.save()