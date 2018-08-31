# 将图片变为iphone5 屏幕尺寸
# iphone5 1136*640

import os
from PIL import Image

ext = ['jpg', 'png']
files = os.listdir('.')


def resizer(img, width=640, hight=1136):
    im = Image.open(img)
    owidth, ohight = im.size
    if owidth <= width and ohight <= hight:
        print("ok~~")
        return

    scale = max(owidth * 1.0 / width, ohight * 1.0 / hight)

    new_im = im.resize((int(owidth / scale), int(ohight / scale)), Image.ANTIALIAS)
    new_im.save('new' + img)
    new_im.close()


if __name__ == '__main__':
    for file in files:
        if file.split('.')[-1] in ext:
            resizer(file)
