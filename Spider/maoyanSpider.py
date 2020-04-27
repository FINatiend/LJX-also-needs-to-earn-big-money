import requests
from requests.exceptions import RequestException
import re
import json
from multiprocessing import Pool

def get_one_page(url,header):
    try:
        response = requests.get(url,headers=header)
        # print(response.status_code)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?(\d+)</i>.*?name"><a.*?>(.*?)</a>.*?star">(.*?)'
                         +'</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    # print(items)
    for item in items:
        yield {
            'index':item[0],
            'title':item[1],
            'actor':item[2].strip()[3:],
            'time':item[3].strip()[5:],
            'scor':item[4]+item[5]

        }

def write_to_file(content):
    with open('film100.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')
        f.close()
def main(offset):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url,header)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__=='__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    pool.close()