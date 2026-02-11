from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Flags para separar os mundos
    is_equipe = models.BooleanField('Membro da Equipe', default=False)
    is_membro = models.BooleanField('Membro da Comunidade', default=True)

    # Campo de controle interno
    email = models.EmailField('E-mail', unique=True)

    # Usaremos o e-mail como login principal no futuro.
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.username} ({'Equipe' if self.is_equipe else 'Membro'})"