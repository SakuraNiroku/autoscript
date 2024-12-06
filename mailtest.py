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
message = MIMEText(f'现在时间为{localtime}\nSend By Github Action','plain','utf-8')
message['From'] = Header(sender)
message['To'] = Header(recv[0])

subject = 'AutoScript Morning News'
message['Subject'] = Header(subject)

with smtplib.SMTP_SSL(host=mail_host,port=465) as server:
        server.login(mail_user,mail_pass)
        server.sendmail(sender,recv,message.as_string())