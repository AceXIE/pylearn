"""
爬虫，爬出网站的照片
"""
import re
import os
import urllib.request

i = 0


def fetch_pic_url(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))
    return picture_url_list


def save(url):
    global i
    picture_name = str(i) + '.jpg'

    try:
        # 请求，并且获取
        urllib.request.urlretrieve(url, picture_name)
        print("Success to download " + url)
    except:
        print("Fail to download " + url)

    i += 1


def fetch_pictures(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    os.chdir(os.path.join(os.getcwd(), 'pictures'))
    for i in range(len(picture_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print("Success to download " + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])


if __name__ == '__main__':
    urls = fetch_pic_url("http://tieba.baidu.com/p/2166231880")
    if not os.path.exists('pictures'):
        os.mkdir('pictures')
    os.chdir(os.path.join(os.getcwd(), 'pictures'))
    for url in urls:
        save(url)
    # fetch_pictures("http://tieba.baidu.com/p/2166231880")
