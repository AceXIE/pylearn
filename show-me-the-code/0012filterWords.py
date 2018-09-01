"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，
当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

import os

path = os.listdir(".")


def load_filter_words(path):
    words = []
    with open(path, 'r', encoding='utf-8') as content:
        words = content.read()
    return words


if __name__ == '__main__':
    words = load_filter_words('filtered_words.txt')
    # print(words)
    s = input("输入：")
    for word in words:
        if word in s:
            s = s.replace(word, '*' * len(word))
    print(s)
