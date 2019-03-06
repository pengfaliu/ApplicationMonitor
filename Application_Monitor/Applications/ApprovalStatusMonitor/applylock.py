#!/usr/bin/python
#coding=utf8
import sys
sys.path.append("/home/dbaops/Shell/public_lib")
import modeloracledml as oradb
import mysqldml as mdb
import os

def writeFile(workdir):
	os.chdir(workdir) ##确认目录

        fobj=open('applylock.sql','r')
        sqls=fobj.read().split('#')
        fobj.close ##记得关闭文件句柄
	
	##wobj = open(writefn,'r+')
        for incre in range(len(sqls)-1): ##遍历每一条sql执行
		splits = sqls[incre].split(';')
		if splits[2]=='oracle':
			conn = oradb.connDB()	
                	columns = oradb.queryColumn(conn,splits[0])
			records=oradb.queryRecord(conn,splits[0])
		elif splits[2]=='mysql':
			connobj = mdb.opdb(database='posloan', host='posloanro.msfinance.db')
			columns = connobj.queryColumn(splits[0]) 
			records = connobj.query(splits[0])
		else:
			print(splits[2],'is error!')

                for record in records:
			print record[0],record[1]
			if record[0]<200 and record[1]<100:
				return 'no'
			else:
				return 'yes'

if __name__=='__main__':
	issend=writeFile('/home/dbaops/Shell/applylock/sqlexecute')
	print issend
