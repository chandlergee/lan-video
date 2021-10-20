from django.http.response import Http404
from django.shortcuts import get_list_or_404, redirect, render
from .models import TVSeries,Movie,Episode,VideoParser

current_parser = VideoParser.objects.first()

def index(request):
    context = {
        'tv_list': TVSeries.objects.all(),
        'mv_list': Movie.objects.all(),
        'parser_list': VideoParser.objects.all(),
        'cur_parser': [current_parser]
    }

    print('xxx',current_parser.name)

    return render(request,'index.html',context)

def episodes(request,id):
    try:
        episodes = get_list_or_404(Episode,tv_id=id)
        return render(request,'episode.html',context={'episodes': episodes,'cur_parser': [current_parser]})
    except Http404 as ex:
        return render(request,'error.html')

def refresh(request,parser_id):
    global current_parser
    try:
        current_parser = VideoParser.objects.get(id=parser_id)
        print(current_parser.name)
        return render(request,'index.html',context={'cur_parser':[current_parser]})
    except Http404 as ex:
        return render(request,'error.html')
    

