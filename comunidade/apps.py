from django.apps import AppConfig

class ComunidadeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comunidade'

    def ready(self):
        # Isso faz o Django ler o arquivo de signals ao iniciar
        import comunidade.signals