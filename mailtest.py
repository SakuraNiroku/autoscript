import smtplib
import os
import time
from email.mime.text import MIMEText
from email.header import Header
import requests

mail_host = os.getenv('mhost')
mail_user = os.getenv('muser')
mail_pass = os.getenv('mpass')
sender = os.getenv('msender')
recv = [os.getenv('mrecv')]

imgget = requests.get('https://www.loliapi.com/acg/pc/?type=json')
imgurl = imgget.json()['url']

localtime = time.asctime(time.localtime(time.time()))
sendText = f'<h1>AutoScript Morning News</h1>'
sendText += f'<p>现在时间为{localtime}</p>'
sendText += f"<p><img src='{imgurl}' height=\"90\" width=\"160\"></p>"
sendText += f'<p>Send By Github Action</p>'
message = MIMEText(sendText,'html','utf-8')
message['From'] = Header(sender)
message['To'] = Header(recv[0])

subject = 'AutoScript Morning News'
message['Subject'] = Header(subject)
with smtplib.SMTP_SSL(host=mail_host,port=465) as server:
        server.login(mail_user,mail_pass)
        server.sendmail(sender,recv,message.as_string())