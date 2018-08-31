import uuid

def genActCode(num):
    codeList=[]
    for i in range(num):
        code = str(uuid.uuid4()).replace("-","").upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace("-", "").upper()
        codeList.append(code)

    for s in codeList:
        print(s)



if __name__ == '__main__':
    genActCode(10)