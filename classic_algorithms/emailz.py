import smtplib
import json

def send_email(recipient, subject, body):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    email = json.loads(open('mail.json').read())['email']
    password = json.loads(open('mail.json').read())['pass']
    smtpObj.login(email, password)
    smtpObj.sendmail(email, recipient,
    'Subject: {0}\n{1}'.format(subject, body))
    {}
    smtpObj.quit()
