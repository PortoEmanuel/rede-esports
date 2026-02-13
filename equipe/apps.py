from django.apps import AppConfig

class EquipeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'equipe'

    def ready(self):
        import equipe.signals  # Isso aqui ativa a mágica