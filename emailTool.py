#! python3
## emailTool.py - Deliver emails

import smtplib,ssl, os
from email.mime.multipart import MIMEMultipart
from datetime import time,datetime,timedelta
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

def sendMail(sub,bod,isTls=True):
    sender = 'Ed Reyes <alerts.digga@gmail.com>'
    receivers = ['eggadigga19@gmail.com']
    cc = ['egga19@yahoo.com', 'eduardo.reyes120@gmail.com']
    receiversAll = receivers + cc
    subject = sub
    body = bod
    server = 'smtp.gmail.com'
    port = 587
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ','.join(receivers)
    msg['CC'] = cc[0]
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # part = MIMEBase('application', "octet-stream")
    # #part_two = MIMEBase('application', "octet-stream")
    # part.set_payload(open(filePath, "rb").read())
    # #part_two.set_payload(open(file_two, "rb").read())
    # encoders.encode_base64(part)
    # #encoders.encode_base64(part_two)
    # part.add_header('Content-Disposition', 'attachment; filename="%s"' %(callsFile))
    # #part_two.add_header('Content-Disposition', 'attachment; filename="%s"' %(file_two))
    # msg.attach(part)
    # #msg.attach(part_two)

    #context = ssl.SSLContext(ssl.PROTOCOL_SSLv3)
    #SSL connection only working on Python 3+
    smtp = smtplib.SMTP(server, port)
    smtp.set_debuglevel(1)
    if isTls:
        smtp.starttls()
    smtp.login('alerts.digga@gmail.com','srhkgeatuyflmrtf')
    smtp.sendmail(sender, receiversAll, msg.as_string())
    print('Email Sent....')
    smtp.quit()


