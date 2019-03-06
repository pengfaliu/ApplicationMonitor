#!/usr/bin/python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        MysqlOperate.py
# Purpose:     provide mysql's operation.
# Author:      liufapeng
# Email:       pengfaliu@16e.com
# Created:     03/09/2016  d/m/y
# Copyright:   (c) liufapeng 2015
# requirement: python >=2.4
# verion : 1.0.0
# Licence:     GPL V2
#-------------------------------------------------------------------------------

#Global variable
import MySQLdb as mdb
import sys
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

class MysqlOperate(object):
    """
    this class contain multiple function 
    init_connection  
    exectue_action
    query
    query_column
    transations
    
    """
    def __init__(self,charset = 'utf8',db_name = '',host = '',db_user = '',
                 db_password = '',db_port = 3306):
        self.charset = charset
        self.host = host
        self.port = db_port
        self.user = db_user
        self.password = db_password
        self.database = db_name 
     
    def init_connection(self):    #connect mysql
        """this is initail connect for mysql ,and get cursor."""
        connect = mdb.connect(host = self.host,port = self.port,user = self.user,
                         passwd = self.password,db = self.database,charset = self.charset)
        return connect
    
    def execute_action(self,*sqls):
        """This function can be use to update,delete,insert,truncate."""
        db = self.init_connection()
        cur = db.cursor()
        for sql in sqls:
            try:
                cur.execute(sql)
                db.commit()
                return True
            except Exception,e:
                db.rollback()
                print e
                return False
            finally:
                db.close()

    def query(self,*sqls): #only use  query
        """This function only be use to query, it return results"""
        db = self.init_connection()
        cur = db.cursor()
        for sql in sqls:
            cur.execute(sql)
            results = cur.fetchall()
            return results
        db.close()

    def query_column(self,*sqls): #only use  query column. 
        db = self.init_connection()
        cur = db.cursor()
        for sql in sqls:
            cur.execute(sql)
            index = cur.description
            return index
        db.close()    
        
        
    def transations(self, sqlArray, *args):
        """this function privde store process operation."""
        if len(sqlArray) <= 0:
            return False;
        db = self.init_connection()
        cur = db.cursor();
        try:
            for index, sql in enumerate(sqlArray):
                arg = args[index] if index in args else ();
                cur.execute(sql, *arg);
                db.commit();
            return True;
        except:
            db.rollback();
            return False;
        finally:
            cur.close();

if __name__=="__main__":
    print "this is mysql dml module"
