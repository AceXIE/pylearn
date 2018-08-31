import redis
import uuid

def genCode(num):
    codeList = []
    for i in range(num):
        code = str(uuid.uuid4()).replace("-", "").upper()
        while code in codeList:
            code = str(uuid.uuid4()).replace("-", "").upper()
        codeList.append(code)
    return codeList

def store(codeList):
    redis.Redis()
    re = redis.Redis(host='127.0.0.1', port=6379, db=0)
    for i in range(len(codeList)):
        re.set(i, codeList[i])

    print(re.get(1))

if __name__ == '__main__':
    store(genCode(10))
