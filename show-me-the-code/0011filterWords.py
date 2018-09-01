"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
"""

import os

path = os.listdir(".")


def load_filter_words(path):
    words=[]
    with open(path, 'r', encoding='utf-8') as content:
        words = content.read()
    return words


if __name__ == '__main__':
    words = load_filter_words('filtered_words.txt')
    # print(words)
    s = input("输入：")
    if s in words:
        print("Freedom")
    else:
        print("Human Rights")
