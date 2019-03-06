#!/usr/bin/python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        OracleOperate.py
# Purpose:     provide oracle's operation.
# Author:      liufapeng
# Email:       pengfaliu@16e.com
# Created:     03/09/2016  d/m/y
# Copyright:   (c) liufapeng 2015
# requirement: python >=2.4
# verion : 1.0.0
# Licence:     GPL V2
#-------------------------------------------------------------------------------


#Global variable
import os
import cx_Oracle as cx_ora
reload(sys)
sys.setdefaultencoding('utf-8')


class OracleOperate(object):
        """
        this class include functions as follow:
        connDB
        closeDB
        queryColumn
        queryRecord
        deleteData
        insertDatas
        writeRecord
        
        """

        #os.environ['NLS_LANG']="SIMPLIFIED CHINESE_CHINA.UTF8"
        os.environ['NLS_LANG']="AMERICAN_AMERICA.AL32UTF8"
        
        def __init__(self,dbdomain = '',username = '',
                     passwd = '',db_port = 1521,sid=''):
                                    
                self.dbdomain = dbdomain
                self.db_port = db_port
                self.username = username
                self.passwd = passwd
                self.sid = sid
                
        
        def init_connection(self):
                #使用makedsn配置tns_name
                tns = cx_ora.makedsn(self.dbdomain,self.db_port,self.sid)
                conn = cx_ora.connect(self.username,self.passwd,tns)
                return conn
        
        def closeDB(self,conn):
                conn.close()
                
        def queryColumn(self,conn,sql):
                cur = conn.cursor() ##可以反复使用
                cur.execute(sql)
                desc = cur.description
                cur.close()
                return desc
        
        def queryRecord(self,conn,sql):
                cur = conn.cursor()
                cur.execute(sql)
                records = cur.fetchall()
                cur.close()
                return records
        
        def deleteData(self,conn,sql):
                cur = conn.cursor()
                cur.execute(sql)      
                cur.close()
                conn.commit()
        
        def insertDatas(self,conn, sql, results):
                cur = conn.cursor()
                cur.prepare(sql)
                cur.executemany(None, results)
                cur.close()
                conn.commit()
        
        def writeRecord(self,conn,readfn):
                fobj = open(readfn,'r')
                sqls = fobj.read().split(';')
                fobj.close ##记得关闭文件句柄
        
                ###conn=connDB() ##打开数据库连接
                for incre in range(len(sqls)-1): ##遍历每一条sql执行
                        columns=queryColumn(conn,sqls[incre])
                        for item in range(len(columns)):
                                print("%-18s" %(columns[item][0])),
                        ##print替换为os.linesep
                        print
        
                        records=queryRecord(conn,sqls[incre])
                        for record in records:
                                for colvalue in record:
                                        print("%-20s" %(str(colvalue))),
                                ##print替换为os.linesep
                                print
                        print
                ##closeDB(conn) ##关闭数据库连接        
                print
                fobj.close()
                

if __name__ == "__main__":
        print "should be unit test."