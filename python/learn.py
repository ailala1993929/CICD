# coding:utf-8
import glob
import os


if __name__ == '__main__':

    path = os.getcwd()
    fileL = glob.glob(path+"\\*.py")
    for file in fileL:
        print file

    print "=================================="
    fileI = glob.iglob(path+"\\*.py")
    for file in fileI:
        print file