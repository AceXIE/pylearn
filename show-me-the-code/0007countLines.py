import os

codes_path = "."
codes = os.listdir(codes_path)


def count_lines(file):
    with open(file, "r", encoding='utf-8', errors='ignore') as content:
        comment = 0
        code = 0
        empty = 0
        res = {}
        code_lines = content.readlines()
        for line in code_lines:
            line.strip()
            if line.startswith("#"):
                comment += 1
            elif line == "":
                empty += 1
            else:
                code += 1
        res["comment:"] = comment
        res["code:"] = code
        res["empty:"] = empty
        return res


if __name__ == '__main__':
    for code in codes:
        # 判断是文件才进行操作
        if os.path.isfile(code) and code.endswith("py"):
         print("code:", code, count_lines(code))
