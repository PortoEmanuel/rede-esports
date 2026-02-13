from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from noticias.views import home, post_detalhe, criar_postagem
from equipe.views import lista_equipe, perfil_colaborador, dashboard_home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', home, name='home'),
    path('noticia/<slug:slug>/', post_detalhe, name='post_detalhe'),
    path('equipe/', lista_equipe, name='lista_equipe'),
    path('equipe/<str:username>/', perfil_colaborador, name='perfil_colaborador'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard_home, name='dashboard_home'),
    path('dashboard/novo/', criar_postagem, name='criar_postagem'),
]

# Isso aqui permite que o Django "sirva" as imagens que você upar no artigo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)