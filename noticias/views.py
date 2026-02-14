from django.shortcuts import render, get_object_or_404, redirect
from .models import Postagem, Categoria
from .forms import PostagemForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from equipe.models import PerfilColaborador

def home(request):
    # Filtra apenas o que está publicado e ordena pela data mais recente
    postagens = Postagem.objects.filter(status='publicado').order_by('-data_publicacao')
    return render(request, 'home.html', {'postagens': postagens})

def post_detalhe(request, slug):
    postagem = get_object_or_404(Postagem, slug=slug, status='publicado')
    
    # Sistema de visualizações baseado em sessão
    # Ele impede que o mesmo usuário dê F5 e gere 1000 visualizações
    session_key = f'post_viewed_{postagem.id}'
    
    if not request.session.get(session_key):
        postagem.visualizacoes += 1
        # O update_fields garante que o Django salve APENAS as visualizações no banco
        postagem.save(update_fields=['visualizacoes'])
        request.session[session_key] = True
    
    return render(request, 'post_detalhe.html', {'post': postagem})

@login_required
def criar_postagem(request):
    # Busca o colaborador logado
    colaborador = get_object_or_404(PerfilColaborador, usuario=request.user, ativo=True)

    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = colaborador
            
            # Lógica para criar Categoria Nova na hora
            nome_nova_cat = form.cleaned_data.get('nova_categoria')
            if nome_nova_cat:
                # get_or_create evita duplicar categorias com o mesmo nome
                nova_cat, created = Categoria.objects.get_or_create(nome=nome_nova_cat)
                post.categoria = nova_cat
            
            # Gera o slug se não existir
            if not post.slug:
                post.slug = slugify(post.titulo)
            
            post.save()
            return redirect('dashboard_home')
    else:
        form = PostagemForm()
    
    return render(request, 'dashboard/criar_postagem.html', {'form': form})

@login_required
def editar_postagem(request, slug):
    postagem = get_object_or_404(Postagem, slug=slug)
    colaborador = get_object_or_404(PerfilColaborador, usuario=request.user, ativo=True)

    # Segurança: Só o autor edita
    if postagem.autor != colaborador:
        return redirect('dashboard_home')

    if request.method == 'POST':
        form = PostagemForm(request.POST, instance=postagem)
        if form.is_valid():
            post = form.save(commit=False)
            
            # Também permite criar nova categoria ao editar
            nome_nova_cat = form.cleaned_data.get('nova_categoria')
            if nome_nova_cat:
                nova_cat, created = Categoria.objects.get_or_create(nome=nome_nova_cat)
                post.categoria = nova_cat
                
            post.save()
            return redirect('dashboard_home')
    else:
        form = PostagemForm(instance=postagem)
    
    return render(request, 'dashboard/criar_postagem.html', {
        'form': form, 
        'editando': True,
        'postagem': postagem
    })