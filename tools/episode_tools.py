import json
import sys
import argparse
import os
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-in','--i',help='input file',required=True)
parser.add_argument('-out','--o',help='output file',required=True)
parser.add_argument('-name','--n',help='episode name prefix',required=True)
parser.add_argument('-url','--u',help='video url prefix',default='')
parser.add_argument('-append','--a',help='append episodes',type=bool,default=False)

args = parser.parse_args(sys.argv[1:])

input_file_data = ''
with open(args.i,'r',encoding='utf-8') as fd:
    input_file_data = fd.read()

soup = BeautifulSoup(input_file_data,features='html.parser')

episodes = []

#if the append flag is enabled,load the old data first,then add the new ones
if args.a is True:
    with open(args.o,'r',encoding='utf-8') as fd:
        episodes.extend(json.loads(fd.read()))

for item in soup.find_all('a'):
    print(item.text)
    episodes.append(
        {
            'name' : '{0} 第{1}集'.format(args.n,item.text),
            'href' : '{0}'.format(args.u) + item.get('data-href',item.get('href','xxxxx'))
        }
    )

with open(args.o,'w',encoding='utf-8') as fd:
    fd.write(json.dumps(episodes,ensure_ascii=False))

print('write data into file {}'.format(args.o))
print('complete!')
