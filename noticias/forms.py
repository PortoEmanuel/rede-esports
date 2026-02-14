from django import forms
from .models import Postagem, Categoria
from equipe.models import FotoGaleria
from django_summernote.widgets import SummernoteWidget

class PostagemForm(forms.ModelForm):
    # Campo para criar categoria na hora
    nova_categoria = forms.CharField(
        max_length=100, 
        required=False, 
        label="Ou crie uma nova categoria",
        widget=forms.TextInput(attrs={'placeholder': 'Nome da nova categoria...', 'class': 'form-control'})
    )

    capa = forms.ModelChoiceField(
        queryset=FotoGaleria.objects.all().order_by('-data_upload'),
        empty_label="--- Sem capa (Matéria apenas texto) ---",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Postagem
        fields = ['titulo', 'subtitulo', 'categoria', 'capa', 'conteudo', 'status']
        widgets = {
            'conteudo': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(PostagemForm, self).__init__(*args, **kwargs)
        # Se a pessoa for criar uma nova categoria, a seleção da antiga não é obrigatória
        self.fields['categoria'].required = False