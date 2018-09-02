"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中.
"""

import json
import xlwt


def json2xls(txt):
    xls_object = xlwt.Workbook()
    sheet = xls_object.add_sheet('city')
    for i in range(len(txt)):
        sheet.write(i, 0, i + 1)
        sheet.write(i, 1, txt[str(i + 1)])
        # data = txt[str(i + 1)]
        # for j in range(len(data)):
        #     sheet.write(i, j + 1, data[j])
    xls_object.save('city.xls')


def load_json(path):
    with open(path, 'r', encoding='UTF-8') as content:
        return json.load(content)


if __name__ == '__main__':
    json_txt = load_json('city.txt')
    json2xls(json_txt)
