"""
将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下

所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!--
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>
"""

import xlrd
from xml.dom import minidom, Node


def openxls():
    workbook = xlrd.open_workbook('numbers.xls')
    num_sheet = workbook.sheet_by_name('numbers')
    sheet_content = []
    for row in range(num_sheet.nrows):
        row_value = num_sheet.row_values(row)
        for i in range(len(row_value)):
            if type(row_value[i]) == float:
                row_value[i] = int(row_value[i])
        sheet_content.append(row_value)
    return sheet_content


def convert2xml(book):
    # Create Dom Object
    doc = minidom.Document()
    # Create root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    # Create 'students' tag
    students = doc.createElement('numbers')
    root.appendChild(students)
    # Create comment element
    students.appendChild(doc.createComment("数字信息"))
    # Create text element
    students.appendChild(doc.createTextNode(str(book)))

    # Save the xml file
    student_xml = open('numbers0019.xml', 'w', encoding='UTF-8')
    student_xml.write(doc.toprettyxml())
    student_xml.close()


if __name__ == '__main__':
    book = openxls()
    convert2xml(book)
