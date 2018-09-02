"""
将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
	城市信息
-->
{
	"1" : "上海",
	"2" : "北京",
	"3" : "成都"
}
</citys>
</root>
"""

import xlrd
from xml.dom import minidom, Node


def openxls():
    workbook = xlrd.open_workbook('city.xls')
    city_sheet = workbook.sheet_by_name('city')
    sheet_content = {}
    for row in range(city_sheet.nrows):
        row_value = city_sheet.row_values(row)
        for i in range(len(row_value)):
            if type(row_value[i]) == float:
                row_value[i] = int(row_value[i])
        sheet_content[str(row + 1)] = row_value[1]
    return sheet_content


def convert2xml(book):
    # Create Dom Object
    doc = minidom.Document()
    # Create root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    # Create 'students' tag
    students = doc.createElement('citys')
    root.appendChild(students)
    # Create comment element
    students.appendChild(doc.createComment("城市信息"))
    # Create text element
    students.appendChild(doc.createTextNode(str(book)))

    # Save the xml file
    student_xml = open('city0017.xml', 'w', encoding='UTF-8')
    student_xml.write(doc.toprettyxml())
    student_xml.close()


if __name__ == '__main__':
    book = openxls()
    convert2xml(book)
