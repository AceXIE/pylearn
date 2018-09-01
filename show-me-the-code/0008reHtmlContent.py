"""
第 0008 题：一个HTML文件，找出里面的正文。
"""

import urllib.request
#
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "http://www.baidu.com"
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page)
    print(soup.body.text)
    print()
