from django.shortcuts import render
from django.http import *
from django.views.generic import ListView
from django.shortcuts import render

from .models import Noticia,Tag


class HomePageView(ListView):
    model = Noticia
    template_name = 'app_noticias/home.html'

def noticias_with_tag(request,tag):
    try:
        teste = Tag.objects.filter(nome=tag)
        todas = Noticia.objects.filter(tags__in=teste).order_by('data_publicacao')
        #tagsNoticia = Noticia.objects.filter

    except tag not in Noticia.tags:
        raise Http404("Não existe essa tag")
    return render(request, 'app_noticias/noticia_tags.html',{'noticia_tag':todas})

def noticia_detalhes(request,noticia_id):
    try:
        noticia = Noticia.objects.get(pk=noticia_id)
    except Noticia.DoesNotExist:
        raise Http404("Noticia nao encontrada")
    return render(request, 'app_noticias/detalhes.html',{'noticia':noticia})

def noticias_resumo_template(request):
    total = Noticia.objects.count()
    return render(request, 'app_noticias/resumo.html',{'total':total})

def noticias_resumo(request):
    total = Noticia.objects.count()
    html="""
    <html>
    <body>
    <h1>Resumo</h1>
    <p>A quantidade total de notícias {}.</p>
    </body>
    </html>
    """.format(total)
    return HttpResponse(html)
