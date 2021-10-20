import os,django


os.environ.setdefault('DJANGO_SETTINGS_MODULE','myapp.settings')
django.setup()

from videos.models import TVSeries,Episode

with open('../tools/data.json','r',encoding='utf-8') as fd:
    import json
    eps = json.loads(fd.read())
    tv = TVSeries.objects.get(id = 3)
    for item in eps:
        ep = Episode(tv_id = tv,e_title = item['name'],e_url = item['href'])
        ep.save()


