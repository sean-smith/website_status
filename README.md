Website Status
==============

This python script will check if your page is online (with status code 200) and send an email and a Yo if it's not.

To Set up:
----------
Set up is simple, clone the repo and then install dependencies. The only dependecy is requests, to install:

    $ sudo pip install requests
    $ git clone https://github.com/sean-smith/website_status.git
    $ cd website_status
    $ pwd                   <== (copy this path for later)
    $ crontab -e

Add in your crontab how often you'd like to check your page. The */5 indicates every 5 mintues:

    */5 * * * * python /path/to/web_status/web_status.py

Next edit the settings.txt file and add in the url, string and email (optionally add in yo username):

    http://addresstocheck.com string_to_find email yo_username
