#!/usr/bin/env python
#coding=utf8
#Filename: mail.py
#Purpose: Send email with txt content or files and image attachment
#Author:  wangbaoshun
#Created: 12/21/2015 d/m/y
#Requirement: python >=2.4
#Version: 1.0.0
#Licence: GPL V2


import smtplib,os
import sys,httplib,urllib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

reload(sys)
sys.setdefaultencoding('utf8')


class SendEmail:
    """
    Function: This class used with send files with email!
    """

    def __init__(self,host,user,passwd,postfix,address):
        """
	Function: Define and init host,user,passwd,postfix and email senders
	host: The mail server address value can be IP or domains
	user: The email account username that can be email address
	passwd: The email account password
	postfix: The email account postfix
	address: The file that strong receivers email address files
	"""
        self._host = host
        self._user = user
        self._passwd = passwd
        self._postfix = postfix
        self._address = address
        
    def _mail_connect(self):
	
        """function: Conection the email server"""
        server = smtplib.SMTP() 
        server.connect(self._host,587)
        server.starttls()
        server.login(self._user,self._passwd)
        self._server = server


    def _get_address(self):
        """Function: Get the receivers email address and convert into list"""
        if os.path.exists(self._address):
            f = open(self._address)
            for i in f:
                addr = i.strip('\n').split(',')
                return addr
            f.close()
        else:
	    print '\033[1;31;40m'
            print 'The'+self._address+'not exists! Please check again!'
	    print '\033[0m'
            os._exit(1)

    def _get_filename(self,files):
	"""
	Function: Get the attachment files filename
	files: The attachement files full path
	"""
        if os.path.exists(files):
            filename = files.split('/')[-1]
            return filename
        else:
            print '\033[1;31;40m'
	    print 'The'+files+'not exits! Please check again'
            print '\033[0m'
            os._exit(2)
            
            
    def sendTxtMail(self,content,subject,subtype='html'):
        """
	function: Send mail with attachments
	content: The email content
	subject: The email subject
	subtype: The email content type, default is html
	"""
        me = self._user
        msg = MIMEMultipart()
        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'))
        msg['Subject'] = subject 
        msg['From'] = me 
        mail_list = self._get_address()
        msg['to'] = ",".join(mail_list)
        
        try: 
	    self._mail_connect()
            self._server.sendmail(me,mail_list,msg.as_string()) 
            self._server.close() 
            return True 
        except Exception,e: 
            print str(e) 
            return False             


    def sendAttachMail(self,content,subject,files,subtype='html'):
        """
	Function: Send mail with attachments
	content: The email content
	subject: The email subject
	files:   The attachment files full path 
	subtype: The email content type, default is html
	"""
        me = self._user 
        msg = MIMEMultipart()
        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'),)
        msg['Subject'] = subject 
        msg['From'] = me 
        mail_list = self._get_address()
        msg['to'] = ",".join(mail_list)
        
        """Add attachment files"""
        filename = self._get_filename(files)
        att1 = MIMEText(open(files).read(),'base64','gb2312')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename='+filename
        msg.attach(att1)
        
        try: 
	    self._mail_connect()
            self._server.sendmail(me,mail_list,msg.as_string()) 
            self._server.close() 
            return True 
        except Exception,e: 
            print str(e) 
            return False         

    def sendImageMail(self,content,subject,images,subtype='html'):
        """
	Function: Send mail with image files
	content: The email content
	subject: The email subject
	images:  The attachment image files full path 
	subtype: The email content type, default is html
	"""
        me = self._user 
        msg = MIMEMultipart()
        msg.attach(MIMEText(content, _subtype=subtype, _charset='utf-8'))
        msg['Subject'] = subject 
        msg['From'] = me 
        mail_list = self._get_address()
        msg['to'] = ",".join(mail_list)\
        
        filename = self._get_filename(images)    
        Image = MIMEImage(open(images,'rb').read())        
        Image.add_header('Content-ID','test')
        Image.add_header('Content-Disposition', 'attachment;filename='+filename)
        msg.attach(Image)
        
        try: 
	    self._mail_connect()
            self._server.sendmail(me,mail_list,msg.as_string()) 
            self._server.close() 
            return True 
        except Exception,e: 
            print str(e) 
            return False         

if __name__ == "__main__":  
    subject = 'subject'
    #content = '<h1>content</h1><br><img src=\"cid:test\" border=\"1\">'
    content = '<h1>content</h1><br>'
    address = '/root/address.ini'
    files = '/root/send.py'
    images = '/root/mm.jpg'

    mail = SendEmail('mail.msxf.com','monitor@msxf.com','d_}IV9lI?|19sf','msxf.com',address)
    mail.sendAttachMail(content, subject,files)
    
    mail.sendImageMail(content,subject,images)
    