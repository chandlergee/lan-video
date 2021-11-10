import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','myapp.settings')
django.setup()

import argparse
import sys
import json
from videos.models import Episode,TVSeries

parser = argparse.ArgumentParser()
parser.add_argument('-name','--n',help='tv series name')
parser.add_argument('-path','--p',help='episodes file')

args = parser.parse_args(sys.argv[1:])

episodes_datas = []

with open(args.p,'r',encoding='utf-8') as fd:
    episodes_datas.extend(json.loads(fd.read()))

if len(episodes_datas) > 0:
    tv = None
    try:
        tv = TVSeries.objects.get(tv_name=args.n)
    except Exception as ex:
        pass
    
    if tv is None:
        tv = TVSeries.objects.create(tv_name=args.n)

    for item in episodes_datas:
        episode = Episode.objects.create(tv_id=tv,e_title=item['name'],e_url=item['href'])

    print('complete!')

else:
    print('no episodes')