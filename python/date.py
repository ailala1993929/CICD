# coding:utf-8

'''
使用中文需要注意编码格式：
SyntaxError: Non-ASCII character
'''
import datetime

DATE_FORMAT = "%Y-%m-%d"  # date to string format

today = datetime.date.today()
print today

before_1xday_ago = today - datetime.timedelta(30 * 1)
print before_1xday_ago

folder = "2020-12-08_sm8350_debug_ssd_20201124"
imagedate_L = folder.split("_")

imgdt = datetime.datetime.strptime(imagedate_L[0], DATE_FORMAT)

imagedate = datetime.date(imgdt.year, imgdt.month, imgdt.day)
print imagedate
