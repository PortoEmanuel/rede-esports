from django.shortcuts import render, get_object_or_404
from .models import PerfilColaborador
from django.contrib.auth.decorators import login_required


def lista_equipe(request):
    membros = PerfilColaborador.objects.filter(ativo=True)
    return render(request, 'equipe/lista.html', {'membros': membros})

def perfil_colaborador(request, username):
    colaborador = get_object_or_404(PerfilColaborador, usuario__username=username)
    

    noticias = colaborador.artigos.filter(status='publicado').order_by('-data_publicacao')
    
    context = {
        'colaborador': colaborador,
        'noticias': noticias
    }
    return render(request, 'equipe/perfil.html', context)




@login_required
def dashboard_home(request):
    try:
        # Tenta pegar o perfil vinculado ao usuário logado
        perfil = request.user.perfil_equipe
        
        # Pega as postagens dele
        minhas_postagens = perfil.artigos.all().order_by('-data_publicacao')
        
        context = {
            'perfil': perfil,
            'postagens': minhas_postagens
        }
        return render(request, 'dashboard/home.html', context)
        
    except PerfilColaborador.DoesNotExist:
        # Se o usuário logou mas NÃO é da equipe, mandamos para uma página de erro ou home
        return render(request, 'dashboard/erro_acesso.html', {
            'mensagem': 'Seu usuário não possui um perfil de colaborador ativo.'
        })