# image package has func like 'open' so we rename it
import PIL.Image as Image
import argparse
import os
import sys

# symbol list,choose different to show pic
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
l = len(ascii_char)
# count how many grays a symbol to represent
# because we have 70 symbols in ascii_char use 256/l=3.xxxx
# then a word can represent 3.xxxx gray or 1-3.xxx use '$' rest are the same manner
unit = 256 / l


def get_char(r, g, b, alfpha=256):
    if alfpha == 0:
        return ' '

    # formula of gray
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # gray //unit get the symbols' index in the list
    return ascii_char[int(gray // unit)]


w, h = 80, 80

if __name__ == '__main__':
    p = sys.path[0]
    # open and reseize img then read all pixels use a symbol instead
    pic = Image.open(p + '/Pics/ascii_dora.png')
    pic = pic.resize((w, h), Image.NEAREST)

    txt = ""

    for i in range(h):
        for j in range(w):
            txt += get_char(*pic.getpixel((j, i)))

        txt += '\n'

    print(txt)
