import smtplib
import os
import time
from email.mime.text import MIMEText
from email.header import Header

mail_host = os.getenv('mhost')
mail_user = os.getenv('muser')
mail_pass = os.getenv('mpass')
sender = os.getenv('msender')
recv = [os.getenv('mrecv')]

localtime = time.asctime(time.localtime(time.time()))
message = MIMEText(f'现在时间为{localtime}\nSend By Github Action')
message['From'] = Header(sender,'utf-8')
message['To'] = Header(recv[0],'utf-8')

subject = 'AutoScript Morning News'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,recv,message.as_string())
except smtplib.SMTPException:
    raise Exception('Cannot send news')