import requests
import smtplib
import time

def is_website_working(url, string_in_page):
    try:
        r = requests.get(url)
        if not string_in_page in r.content or r.status_code !=200:
            return False
        return True
    except:
        return False

def send_mail(url):
    s = smtplib.SMTP('localhost')
    s.sendmail("seanwssmith@gmail.com", ["seanwssmith@gmail.com"], "WEBSITE DOWN"+ url)
    s.quit()

def main():
    





print is_website_working("http://54.148.80.59:82/", "Sean")
send_mail("url")
