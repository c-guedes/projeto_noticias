from django.urls import path
from . import views
from app_noticias.views import noticias_resumo, HomePageView,noticias_resumo_template,noticia_detalhes,noticias_with_tag

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('noticias/resumo/', noticias_resumo,name='request'),
    path('resumo/', noticias_resumo_template,name='request'),
    path('detalhe/<int:noticia_id>', noticia_detalhes,name='detalhes'),
    path('detalhe/noticia_tags/<str:tag>', noticias_with_tag,name='noticeWithTag'),
    
]
