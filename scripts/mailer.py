import smtplib
import json

def send_email_gmail(gmail_user, gmail_password):

    with open(fileDir + '\mailer.config.json', 'r') as f:
        config = json.load(f)

    gmail_user = config['authentication']['user']
    gmail_password =  config['authentication']['password']

    sent_from = gmail_user  
    to = config['authentication']['to']
    subject = 'OMG Super Important Message'  
    body = 'Hey, whats up?\n\n- You'

    email_text = """\  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print("Email sent")
    except Exception as e: 
        print(e)
        print("Something went wrong...")