import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/movie/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

res = requests.get(url, headers=headers)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

titleSoupList = soup.select('div.title')
print(soup)