#!/usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        query.py
# Purpose:     Send SMS by Zabbix monitor
# Author:      wangbaoshun
# Email:       baoshun.wang@msfinance.cn
# Created:     13/07/2015  d/m/y
# Copyright:   (c) wangbaoshun 2015
# requirement: python >=2.4
# verion : 1.0.0
# Licence:     GPL V2
#-------------------------------------------------------------------------------

import os
import requests
import json
import uuid
import sys
import httplib
import urllib


reload(sys)
sys.setdefaultencoding('utf8')

class SmsSender(object):
    """
    this class use third party short message interface to send . 
    """
    def __init__(self,url="http://notification.msxf.lo/SMS/sendSingleSMS"):
            
        # Define sms variable
        self.SerialNumber = "".join(str(uuid.uuid1(node=None, clock_seq=None)).split('-'))
        self.url = url
        #phone_number = str(sys.argv[1])
        #content = sys.argv[2]
        
    def send_sms(self,content,phone_number):
        try:
            resp = requests.post((self.url),
            data={
                "SourceSerialNumber": self.SerialNumber,
                "sourceBizSystem": "maintenance",
                "sourceBizType": "maintenance_Warning",
                "mobileNumber": phone_number,
                "msgParam": content,
                "type": "json"
            },timeout=3 , verify=False);
            return True
        except Exception,e:
            print e
            return False
        
        result =  json.loads(resp.content)
        message =  eval(json.dumps(result))
        
        if int (eval(json.dumps(result))['code']) == 0:
            print "短信发送成功"
            return True
        else:
            print "短信发送失败"
            return False
            #send_mail(persons, '短信发送失败',str(message))

if __name__ == "__main__":
    t = SmsSender()
    t.send_sms("test", "13717861624")
