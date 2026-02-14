from django.shortcuts import render, get_object_or_404, redirect
from .models import PerfilColaborador, FotoGaleria
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from noticias.models import Postagem
from django.db.models import Sum

# FUNÇÃO QUE ESTAVA FALTANDO: Lista de todos os membros (página pública)
def lista_equipe(request):
    membros = PerfilColaborador.objects.filter(ativo=True)
    return render(request, 'equipe/lista.html', {'membros': membros})

# FUNÇÃO QUE ESTAVA FALTANDO: Perfil individual do colaborador (página pública)
def perfil_colaborador(request, username):
    colaborador = get_object_or_404(PerfilColaborador, usuario__username=username, ativo=True)
    noticias = Postagem.objects.filter(autor=colaborador, status='publicado').order_by('-data_publicacao')
    
    context = {
        'colaborador': colaborador,
        'noticias': noticias
    }
    return render(request, 'equipe/perfil.html', context)

# Dashboard do Colaborador (Página restrita)
@login_required
def dashboard_home(request):
    try:
        perfil = PerfilColaborador.objects.get(usuario=request.user, ativo=True)
        cargos_nomes = perfil.cargos.values_list('nome', flat=True)
        
        # Identifica se é escritor ou fotógrafo
        e_escritor = any(c in ['Escritor', 'Editor', 'Admin', 'Redator'] for c in cargos_nomes)
        e_fotografo = 'Fotógrafo' in cargos_nomes
        
        context = {
            'perfil': perfil,
            'e_escritor': e_escritor,
            'e_fotografo': e_fotografo,
            'cargos_lista': cargos_nomes,
            'total_visualizacoes': 0,
        }
        
        # Dados específicos para Escritores
        if e_escritor:
            postagens = Postagem.objects.filter(autor=perfil).order_by('-data_publicacao')
            context['postagens'] = postagens
            total_v = postagens.aggregate(total=Sum('visualizacoes'))['total']
            context['total_visualizacoes'] = total_v or 0

        # Dados específicos para Fotógrafos
        if e_fotografo:
            context['minhas_fotos'] = FotoGaleria.objects.filter(fotografo=perfil).order_by('-data_upload')
        
        return render(request, 'dashboard/dashboard.html', context)
        
    except PerfilColaborador.DoesNotExist:
        return render(request, 'dashboard/erro_acesso.html', {
            'mensagem': 'Seu usuário não possui um perfil de colaborador vinculado ou ativo.'
        })

# Ação de upload para o Fotógrafo
@login_required
def upload_foto(request):
    if request.method == 'POST' and request.FILES.get('imagem'):
        perfil = get_object_or_404(PerfilColaborador, usuario=request.user)
        titulo = request.POST.get('titulo', 'Sem título')
        imagem = request.FILES.get('imagem')
        
        FotoGaleria.objects.create(
            titulo=titulo,
            imagem=imagem,
            fotografo=perfil
        )
    return redirect('dashboard_home')

# Logout do sistema
def logout_view(request):
    logout(request)
    return redirect('home')