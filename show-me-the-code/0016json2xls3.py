"""
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]
请将上述内容写到 numbers.xls 文件中
"""

import json
import xlwt


def json2xls(txt):
    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('numbers')
    for i in range(len(txt)):
        data = txt[i]
        for j in range(len(data)) :
            sheet.write(i, j, data[j])
    xls_object.save('numbers.xls')


def load_json(path):
    with open(path, 'r', encoding='UTF-8') as content:
        return json.load(content)


if __name__ == '__main__':
    json_txt = load_json('numbers.txt')
    json2xls(json_txt)
