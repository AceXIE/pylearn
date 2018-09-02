"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
请将上述内容写到 student.xls 文件中。
"""

import json
import xlwt


def json2xls(txt):
    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('student')
    for i in range(len(txt)):
        sheet.write(i, 0, i + 1)
        data = txt[str(i + 1)]
        for j in range(len(data)):
            sheet.write(i, j + 1, data[j])
    xls_object.save('student.xls')


def load_json(path):
    with open(path, 'r', encoding='UTF-8') as content:
        # cnt = content.read()
        return json.load(content)


if __name__ == '__main__':
    json_txt = load_json('student.txt')
    json2xls(json_txt)
