# coding:utf-8

import os

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
list1 = [('TMP', 'C:\\Users\\annie.wu\\AppData\\Local\\Temp'), ('PYTHONIOENCODING', 'UTF-8'), ('COMPUTERNAME', 'ANNIE-WU-PC')]
list2 = [1,2,3,4]
list3 = [(1),(2),(3),(4)]
tuple1 = (1,2,3,4)
dict1 = {'a':1,'b':2,'c':3}

environ = os.environ
stringE = str(environ)#字符串包装
NstringE = stringE.replace("\\\\","\\")#字符串替换
listE = (NstringE.split(',')) #字符串分割

def printInfo():
    print "获取当前目录：" + os.getcwd()
    print os.path.basename(os.getcwd())
    print os.path.dirname(os.getcwd())


def getType(string):
    type = None
    if isinstance(string,int):
        type = "int"
    elif isinstance(string,str):
        type = "string"
    elif isinstance(string,list):
        type = "list"
    elif isinstance(string,float):
        type = "float"
    elif isinstance(string,tuple):
        type = "tuple"
    elif isinstance(string,dict):
        type = "dict"
    elif isinstance(string,set):
        type = "set"
    return type

def printEnviron():
    # print environ
    # print getType(environ)
    # stringE = str(environ)#字符串包装
    # NstringE = stringE.replace("\\\\","\\")#字符串替换
    # listE = (NstringE.split(',')) #字符串分割
    # print listE
    print getType(listE)
    print listE
    for i in listE:
        print i

def getEnvironName():
    listEnviron = []
    for i in listE:
        listEnviron.append(i.split(': ')[0])
        # i.split(': ')[0]

    # print listEnviron
    for i in listEnviron:
        print i


if __name__ == '__main__':
    printInfo()

    print getType(123)
    print getType("123")
    print getType(list1)
    print getType(list2)
    print getType(list3)
    print getType(123.0)
    print getType(tuple1)
    print getType(dict1)
    print getType(sites)

    printEnviron()#按行输出环境变量
    getEnvironName()


