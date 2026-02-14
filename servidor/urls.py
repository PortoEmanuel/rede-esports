from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Imports das Views de Noticias
from noticias.views import home, post_detalhe, criar_postagem, editar_postagem

# Imports das Views de Equipe (Adicionei o upload_foto aqui)
from equipe.views import (
    lista_equipe, 
    perfil_colaborador, 
    dashboard_home, 
    logout_view, 
    upload_foto
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    
    # Home e Notícias
    path('', home, name='home'),
    path('noticia/<slug:slug>/', post_detalhe, name='post_detalhe'),
    
    # Equipe Pública
    path('equipe/', lista_equipe, name='lista_equipe'),
    path('equipe/<str:username>/', perfil_colaborador, name='perfil_colaborador'),
    
    # Autenticação
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Dashboard e Ações de Colaborador
    path('dashboard/', dashboard_home, name='dashboard_home'),
    path('dashboard/novo/', criar_postagem, name='criar_postagem'),
    path('dashboard/editar/<slug:slug>/', editar_postagem, name='editar_postagem'),
    
    # A Rota que o José vai usar para subir as fotos
    path('dashboard/upload-foto/', upload_foto, name='upload_foto'),
]

# Configuração para servir arquivos de mídia (fotos) em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)