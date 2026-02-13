from django import forms
from .models import Postagem
from django_summernote.widgets import SummernoteWidget

class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        # Liberamos o que o redator mexe, escondemos autor e visualizações
        fields = ['titulo', 'subtitulo', 'categoria', 'capa', 'conteudo', 'status']
        widgets = {
            'conteudo': SummernoteWidget(), # Aqui a mágica acontece!
        }