from bs4 import BeautifulSoup
import json

WRITE_FILE_PATH = 'data.json'
READ_FILE_PATH = '1.html'

def load_html(path,encoding='utf-8'):
    with open(path,'r',encoding=encoding) as fd:
        return fd.read()

def write_html(path,datas,encoding='utf-8'):
    with open(path,'w',encoding=encoding) as fd:
        fd.write(datas)

href_list = []
soup = BeautifulSoup(load_html(READ_FILE_PATH))
for item in soup.find_all('a'):
    x = dict()
    x['name'] = '平凡的世界 第{}集'.format(str(item.contents[0]).strip())
    x['href'] = 'https://v.qq.com/' + item['href']
    href_list.append(x)

write_html(WRITE_FILE_PATH,json.dumps(href_list,ensure_ascii=False))

    
