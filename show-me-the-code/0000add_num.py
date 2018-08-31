# https://github.com/Show-Me-the-Code/show-me-the-code
# 第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
# 需要安装PIL库

from PIL import Image, ImageFont
from PIL import ImageDraw

def add_num(picPath, num):
    img = Image.open(picPath)
    img = img.convert('RGB')
    x, y = img.size
    print(x,y)
    # myfont = ImageFont.truetype('Futura.ttf', x / 3)
    # Image.Draw(img).text((2 * x / 3, 0), str(num), fill = 'red')
    # Image.
    # img.save('pic_with_num.jpg')
    # Image._show(img)
    font = ImageFont.truetype("Futura.ttf", 16)
    ImageDraw.Draw(img).text((0, 0), str(num), (255, 0, 0), font=font)
    img.save('sample-out.jpg')


if __name__ == '__main__':
    add_num('pic.jpg', 9)