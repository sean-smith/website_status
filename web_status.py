#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import smtplib

exec(open(inemail.py))


def is_website_working(url, string_in_page):
    try:
        r = requests.get(url)
        if not string_in_page in r.content or r.status_code !=200:
            return False
        return True
    except:
        return False

def send_mail(url, email):
    sender = email
    receiver = [email]

    message = """From: <"""+email+""">
    To: <"""+email+""">
    Subject: WEBSITE MAIL

    Your website """+url+ """ is down!.
    """

    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receiver, message)
       print "Successfully sent email"
    except:
       print "Error: unable to send email"

def send_yo(username, url):
    data={'api_token': "8784db87-d95d-4fad-92d6-3e1a10bd4200", 'username': username}
    data["link"] = url
    r = requests.post("http://api.justyo.co/yo/", data)
    return r.status_code

def main():
    f = open("/home/ec2-user/website_status/settings.txt", "r")
    for line in f:
        #print line
        if line[0] != "#":
            params = line.split()
            #print(params)
            if len(params) < 3:
                print "There must be at least three parameters (yo_username is optional)"
                print "url string email yo_username"
                return False
            url = params[0]
            string = params[1]
            email = params[2]
            yo_username = ""
            if len(params) == 4:
                yo_username = params[3]
            if not is_website_working(url, string):
                if yo_username != "":
                    send_yo(yo_username, url)
                
		send_mail(url, email)
                print "Website "+url+" down :("
            else:
                print "Website "+url+" running status 200 :)"



if __name__ == '__main__':
    main()
