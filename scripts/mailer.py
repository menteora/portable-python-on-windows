import smtplib
import json
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_gmail():

    fileDir = os.path.dirname(os.path.abspath(__file__))
    parentDir = os.path.dirname(fileDir) 
    logPath = os.path.join(parentDir, 'logs') 
    log_files = os.listdir(logPath)

    for index, log_file in enumerate(log_files):
        log_files[index] = logPath + "\\" + log_file


    with open(fileDir + '\mailer.config.json', 'r') as f:
        config = json.load(f)

    gmail_user = config['authentication']['user']
    gmail_password =  config['authentication']['password']

    fromaddr = gmail_user
    toaddr = ', '.join(config['authentication']['to']) 
    print(toaddr)
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SUBJECT OF THE EMAIL"
 
    body = "TEXT YOU WANT TO SEND"
 
    msg.attach(MIMEText(body, 'plain'))
 
    filename = "executor.log"
    attachment = open("logs\\" + filename, "rb")
 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)


    try:  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()
        server.sendmail(fromaddr, config['authentication']['to'], text)
        server.close()

        print("Email sent")
    except Exception as e: 
        print(e)
        print("Something went wrong...")

send_email_gmail()