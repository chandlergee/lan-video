import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','myapp.settings')
django.setup()

from videos.models import TVSeries,Episode

x = TVSeries(tv_name='平凡的世界',tv_country = '华语',tv_mtype = '家庭',tv_description = '略')
x.save()



