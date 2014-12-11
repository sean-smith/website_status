#!/usr/bin/python
import requests
import smtplib

def is_website_working(url, string_in_page):
    try:
        r = requests.get(url)
        if not string_in_page in r.content or r.status_code !=200:
            return False
        return True
    except:
        send_mail(url)
        return False

def send_mail(url):
    sender = 'seanwssmith@gmail.com'
    receivers = ['seanwssmith@gmail.com']

    message = """From: From Person <seanwssmith@gmail.com>
    To: To Person <seanwssmith@gmail.com>
    Subject: WEBSITE MAIL

    Your website is down!.
    """

    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receivers, message)
       print "Successfully sent email"
    except:
       print "Error: unable to send email"



def send_yo(username, url):
    data={'api_token': "048fd446-d462-4524-93c0-ad644d3387ee", 'username': username}
    data["link"] = url
    r = requests.post("http://api.justyo.co/yo/", data)
    return r.status_code






def main():
    return 2





print is_website_working("http://seanssmith.me/", "Sean")
send_mail("url")
