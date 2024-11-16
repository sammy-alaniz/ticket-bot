from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# html = urlopen('https://google.com')
# html = urlopen('https://www.showclix.com/events/31087')

# bs = BeautifulSoup(html.read(), 'html.parser')
# print(bs)
# print(bs.h1)


from urllib.request import urlopen, Request

url = 'https://www.showclix.com/events/31087'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

req = Request(url, headers=headers)
html = urlopen(req).read()

print(html)