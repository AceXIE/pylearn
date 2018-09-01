import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':

    url = "http://www.baidu.com"
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page)
    links = soup.findAll('a')
    for link in links:
        print(link['href'])
