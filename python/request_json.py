#!/bin/python

import sys
import json
import urllib2


class request_json(object):
    def __init__(self):
        pass

    def http_post(self):
        url='http://1.116.54.237:8088/api/ailala/login'
        values ={'user':'admin','passwd':'Cc668866'}
        jdata=json.dumps(values)
        req = urllib2.Request(url,jdata)
        response = urllib2.urlopen(req)
        print response
        return response

    def http_get(self):
        url='http://1.116.54.237:8088/api/ailala/loadData'
        response=urllib2.urlopen(url)
        print response.read()
        return response.read()

    def json_prase(self,jsondata):
        res = json.loads(jsondata)
        print res
        return res

    def Excute(self):
        self.http_get()
        self.http_post()
        # jsondate = self.http_get()
        # self.json_prase(jsondate)


def main():
    sys.exit(request_json().Excute())

if __name__ == '__main__':
    main()