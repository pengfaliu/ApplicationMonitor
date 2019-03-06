#!/usr/bin/python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        Config_ini_Parser.py
# Purpose:     provide mysql's operation.
# Author:      liufapeng
# Email:       pengfaliu@16e.com
# Created:     03/09/2016  d/m/y
# Copyright:   (c) liufapeng 2015
# requirement: python >=2.6
# verion : 1.0.0
# Licence:     GPL V2
#-------------------------------------------------------------------------------

import sys
from ConfigParser import ConfigParser

class PaserConfig(object):
    """
    this class shuld be parser .ini configure file. include function as follow
    get_oracle_db_info
    get_mysql_db_info
    get_sms_info
    get_mail_info
    """
    
    def __init__(self,conf_file_path=''):
        self.conf_file_path = conf_file_path
        self.parser = ConfigParser()
        self.parser.read(self.conf_file_path)
        
    def get_oracle_db_info(self,oracle_section = "OracleDbInfo"):
        """ 
        section must be "OracleDbInfo" in ini file,like this
        
        #x.domain.lo also is right 
        [OracleDbInfo]
        dbdomain = 192.168.1.1 
        db_port = 1521
        username = username
        passwd = passwd
        sid = sid
        
        """
        info = self.parser.items(oracle_section) #tuples in list 
        return dict(info)

    def get_mysql_db_info(self,mysql_section = "MysqlDbInfo"):
        """ 
        section must be "MysqlDbInfo" in ini file,like this
        
        #both ip adress and domain are right.
        [MysqlDbInfo]
        charset = charset
        host = host 
        port = db_port
        user = db_user
        password = db_password
        database = db_name
        
        """
        info = self.parser.items(mysql_section) #tuples in list 
        return dict(info)
    
    def get_sms_info(self,sms_section = "SmsInfo"):
        """
        this function can get mobile number from diffrent department, return a list with mobile number.
        
        [SmsInfo]
        dev_department = (fapeng.liu:13112121313),(shuqiang.yang:13211111453)
        sre_department = (fapeng.liu:13112121313),(shuqiang.yang:13211111453)
        risk_department = (fapeng.liu:13112121313),(shuqiang.yang:13211111453)
        ...
        
        """
        TMP= []
        mobile_num = []
        info = dict(self.parser.items(sms_section))
        num_list = [x for x in info.values()]
        for tmp in num_list:
            TMP.extend(tmp.split(','))
        
        for tmp in TMP:
            try:
                mobile_num.append(tmp.split(":")[1].rstrip(')'))
            except Exception,e:
                print e,
                sys.exit(1)            
        return mobile_num
        
     
    def get_mail_info(self,mail_section = "MailInfo"):
        """
        this function can get mail address from diffent department. return a mail address list
        """
        mails= []
        info = dict(self.parser.items(mail_section))
        mail_list = [x.split(",")  for x in info.values()]
        for tmp in mail_list:
            mails.extend(tmp)
        
        return mails
    
    def _self_define(self,section=""):
        """
        this function will be provide generation method. you can define yours section
        and return a dictionary object.
        """
        
        info = self.parser.items(section)
        return dict(info)
    
if __name__ == "__main__":
    test = PaserConfig(conf_file_path='template.conf')
    print test.get_mysql_db_info()
    print test.get_oracle_db_info()
    print test.get_sms_info()
    print test.get_mail_info()
    