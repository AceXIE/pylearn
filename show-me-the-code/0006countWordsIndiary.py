import re
import os

# set diaries path
diaries_path = "diaries/"
diaries = os.listdir(diaries_path)


def countHighestList(diary_list):
    word_diaries = {}
    for word in diary_list:
        if word.lower() not in word_diaries:
            word_diaries[word.lower()] = 0
        else:
            word_diaries[word.lower()] += 1

    key = sorted(word_diaries, key=word_diaries.__getitem__, reverse=True)[0:5]
    return key


if __name__ == '__main__':
    # 操作文件
    for diary in diaries:
        with open(diaries_path + diary, 'r') as con:
            diary_list = re.findall(r"[\w]+", con.read())
            print("diary:", diary, countHighestList(diary_list))
