import requests
import re
import time

local = time.strftime("%Y.%m.%d")
url = 'http://cn.bing.com/'
con = requests.get(url)
content = con.text
reg = r"(/az/hprichbg/rb/.*?.jpg)"
findall = re.findall(reg, content, re.S)
print(findall)
a = findall[0]
print(a)
read = requests.get("https://cn.bing.com/"+a)
f = open('%s.jpg' % local, 'wb')
f.write(read.content)
f.close()