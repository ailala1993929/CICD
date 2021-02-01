import re

project_name = "platform/vendor/zeusis/zui/app/BsUserLearning"
revision = "aaa"
upstream = "bsui_release5.0_apk"


def replaceRevi():
    with open('SM8350_R_DEV_BSUI_20200916.xml','r+') as f:
        with open('newrevison.xml','r+') as fw:
            lineLst = f.readlines()
            for line in lineLst:
                if line.__contains__(project_name):
                    if revision.strip():
                        matchRevisObj = re.search(r'revision=(".*?")', line, re.M|re.I)
                        if line.__contains__(matchRevisObj.group()):
                            newLine = line.replace(matchRevisObj.group(),'revison="%s"' %revision)
                            fw.writelines(newLine)
                    continue
                fw.writelines(line)


def replaceUpstr():
    with open('newrevison.xml','r+') as fw:
        with open('newupstream.xml','r+') as fwu:
            lineLstR = fw.readlines()
            for lineR in lineLstR:
                if lineR.__contains__(project_name):
                    if upstream.strip():
                        matchUpstr = re.search(r'upstream=(".*?")', lineR, re.M|re.I)
                        if lineR.__contains__(matchUpstr.group()):
                            newLineR = lineR.replace(matchUpstr.group(),'upstream="%s"' %upstream)
                            fwu.writelines(newLineR)
                    continue
                fwu.writelines(lineR)


if __name__ == '__main__':
    replaceRevi()
    replaceUpstr()