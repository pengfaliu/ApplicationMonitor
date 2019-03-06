 #!/usr/bin/python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        createExcel.py
# Author:      ranyuan
# Email:       yuan.ran@msxf.com	
# Created:     23/02/2016
# requirement: python >=2.6
#-------------------------------------------------------------------------------
import xlsxwriter
#import mysqldml   # this is for the example at end of page

class ExcelGenerator(object):
    def __init__(self,excelname):
        self.excelname = excelname

    # create a excel file
    def createExcel(self):
        workbook = xlsxwriter.Workbook(self.excelname)
        return  workbook

    # create Sheet if have many sheet in one excel file
    def createSheet(self,workbook,sheetName,queryColumnResult,queryResult):
        worksheet = workbook.add_worksheet(sheetName)
        #ops = opdb(charset='utf8')
        # process column name to excel
        colres = queryColumnResult
        bold = workbook.add_format({'bold':True})
        row ,col = 0, 0
        for info in colres:
            #print str(info[0])+"  ",
            worksheet.write(row,col,str(info[0]),bold)
            col = col +1

        # process values  to excel
        result = queryResult
        row , col = 1, 0
        for info in result:
            #print info
            for object in info:
                # str(object)+"  ",
                worksheet.write(row,col,str(object))
                col =col + 1
            col = 0
            row = row + 1

    # close file
    def closeExcel(self,workbook):
        workbook.close()

    # this is a example 
#if __name__=="__main__":

#    sql1="select apply_no,id ,person_name,person_ident,person_id_unique  from cont_loan_apply limit 3"
#    sql2="select apply_no,id ,person_ident,person_id_unique  from cont_loan_apply limit 8"
#    dbins = mysqldml.opdb(charset='utf8') #初始化数据库实例
#    excelproin = excelpro('/home/dbaops/demo2.xlsx') #初始化excel实例
#    workbook = excelproin.createExcel() #创建excel表
#    queryColumnResult = dbins.queryColumn(sql1) #获取查询的字段名结果是个列表
#    queryResult = dbins.query(sql1) #获取查询的具体行的数据结果也是个列表
#    excelproin.createSheet(workbook,"sheet1",queryColumnResult,queryResult) #将sql1执行的结果放到sheet1中
#    queryColumnResult = dbins.queryColumn(sql2)
#    queryResult = dbins.query(sql2)
#    excelproin.createSheet(workbook,"sheet2",queryColumnResult,queryResult)
#    excelproin.closeExcel(workbook) #最后关闭excel实例
