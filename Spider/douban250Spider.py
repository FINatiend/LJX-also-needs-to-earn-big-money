import requests
from requests.exceptions import RequestException
import re
import json

def get_one_page(url,header):
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    # pattern = re.compile('<li>.*?title">(.*?)</span>.*?playable">(.*?)</span>'
    #                      +'class="">(.*?)<br>',re.S)
    pattern = re.compile('<li>.*?class="">(\d+)</em>.*?title">(.*?)</span>.*?title">.*?class="">(.*?)<br>'
                         + '(.*?)</p>.*?average">(.*?)</span>.*?</li>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        print(item)
        yield {
            'index':item[0],
            'title':item[1],
            'people':item[2].strip().replace('&nbsp;',''),
            'time':item[3].strip().replace('&nbsp;',''),
            'score':item[4]
        }

def write_to_file(content):
    with open('douban250.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(num):
    url = 'https://movie.douban.com/top250?start='+str(num)+'&filter='
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    html = get_one_page(url,header)
    print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(i*25)