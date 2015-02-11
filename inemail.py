__author__ = 'bernardo'


import csv
import mechanize
import re
import time
import BeautifulSoup
import smtplib

def sendEmail(result, sfrom, pwd, sto):
    SMTP_SERVER = 'smtp.live.com'
    SMTP_PORT = 587

    sender = 'sfrom'
    recipient = 'sto'
    subject = 'Promocoes'
    body = result

    body = "<b>" + body + "<b>"

    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(SMTP_SERVER , SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, pwd)

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()
