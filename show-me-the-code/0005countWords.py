import re

def count(txt):
    pattern = re.compile('[a-zA-Z]+')
    words = pattern.findall(txt)
    dict = {}
    for i in words:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1
    print(dict)

if __name__ == '__main__':
    path = '0005words.txt'
    with open(path,'r') as file:
        data = file.read()
        print(data)
    # count("I love")
    count(data)