from django.shortcuts import render, get_object_or_404
from .models import Postagem
from django.shortcuts import redirect
from .forms import PostagemForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

def home(request):
    # Trocamos 'order_set' por 'order_by'
    postagens = Postagem.objects.filter(status='publicado').order_by('-data_publicacao')
    
    return render(request, 'home.html', {'postagens': postagens})


def post_detalhe(request, slug):
    postagem = get_object_or_404(Postagem, slug=slug, status='publicado')
    
    session_key = f'visualizado_{postagem.id}'

    if not request.session.get(session_key):
        postagem.visualizacoes += 1
        postagem.save()
        request.session[session_key] = True
    
    return render(request, 'post_detalhe.html', {'post': postagem})


@login_required
def criar_postagem(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST, request.FILES)
        if form.is_valid(): # <--- O fix está aqui!
            post = form.save(commit=False)
            post.autor = request.user.perfil_equipe
            
            # Gera o slug automaticamente se estiver vazio
            if not post.slug:
                post.slug = slugify(post.titulo)
                
            post.save()
            return redirect('dashboard_home')
    else:
        form = PostagemForm()
    
    return render(request, 'dashboard/criar_postagem.html', {'form': form})