from PIL import Image, ImageDraw, ImageFont
import string
import random


def random_letters(cnt):
    return ' '.join(random.choice(string.ascii_letters) for x in range(cnt))


def draw(letters):
    # Set the size of the image
    width = 100
    height = 40

    # Generate an image
    im = Image.new("RGB", (width, height), (255, 255, 255))

    dr = ImageDraw.Draw(im)
    for i in range(len(letters)):
        font = ImageFont.truetype("Futura.ttf", 30)
        dr.text((5 + i * 10, 5), letters[i], (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                font)
    del dr

    # Change the background color
    for x in range(width):
        for y in range(height):
            if im.getpixel((x, y)) == (255, 255, 255):
                im.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    # Save the image
    im.save('t1.png')


if __name__ == '__main__':
    # print(string.ascii_letters)
    # print(random.choice(string.ascii_letters))
    letters = random_letters(4)
    # letters.upper()
    print(letters)
    draw(letters)
