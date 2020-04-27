import requests
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
content = requests.get('https://book.douban.com/',headers=header)
print(content)
content = content.text
# print(content)
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>',re.S)
results = re.findall(pattern,content)
print(results)
# for result in results:
#     url,name,author,date = result
#     print(url,name,author,date)