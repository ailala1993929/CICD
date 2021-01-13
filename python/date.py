# coding:utf-8

import datetime


DATE_FORMAT = "%Y-%m-%d"  # date to string format 设置日期格式
ODVB_BASE_PATTERN = "/dailybuild/odvb/%s/*"

today = datetime.date.today()
print today

before_1xday_ago = today - datetime.timedelta(30 * 1)
print before_1xday_ago

folder = "2020-12-08_sm8350_debug_ssd_20201124"
imagedate_L = folder.split("_")
print imagedate_L

imgdt = datetime.datetime.strptime(imagedate_L[0], DATE_FORMAT)
print imgdt

imagedate = datetime.date(imgdt.year, imgdt.month, imgdt.day)
print imagedate

