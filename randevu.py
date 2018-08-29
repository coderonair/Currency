# import libraries
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
from notify_run import Notify
import os
import json


import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate



def getUSD():
    # specify the url
    quote_page = "http://randevu.bezmialemhastanesi.com/randevu/get_app_time.php?dr_id=3083&dept_id=1215&day=04.09.2018"
    quote_page2 = "http://randevu.bezmialemhastanesi.com/randevu/get_app_time.php?dr_id=3083&dept_id=1215&day=03.09.2018"
    quote_page3 = "http://randevu.bezmialemhastanesi.com/randevu/get_app_time.php?dr_id=3060&dept_id=610&day=04.09.2018"
    quote_page4 = "http://randevu.bezmialemhastanesi.com/randevu/get_app_time.php?dr_id=2516&dept_id=1287&day=03.09.2018"

    j = urllib2.urlopen(quote_page)
    j_obj = json.load(j)

    print j_obj

    jsonData = j_obj["Rows"]
    for item in jsonData:
        day1 = item.get("day")
        time1 = item.get("time")
        print("day1==  " + day1.encode('utf-8'))
        print("time1==  " + time1.encode('utf-8'))



    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Next, log in to the server
    server.login("afpsoft", "anahtaranahtar")

    # Send the mail
    fromadd = "afpsoft@gmail.com"
    toadd1 = "alipiskin@gmail.com"
    toadd2 = "afpsoft@gmail.com"




    # notify = Notify()
    # notify.send(msg)

    msg1 = "RANDEVU KAPALI:  " + day1.encode('utf-8')
    msg2 = "RANDEVU DOLU:  " + day1.encode('utf-8')
    msg3= "!!!RANDEVU AÇILDI !!!:  " + day1.encode('utf-8')
    command1 ="curl https://notify.run/pwIkd1EewIG3SpTy -d " + "\"" + msg1 + "\""
    command2 ="curl https://notify.run/pwIkd1EewIG3SpTy -d " + "\"" + msg2 + "\""
    command3 = "curl https://notify.run/pwIkd1EewIG3SpTy -d " + "\"" + msg3 + "\""



    if day1.encode('utf-8')=="<font color=#CC0000><b>Kapalı</b></font>":
        msg = msg1
        print "KAPALI"
        #os.system(command1)

    if day1.encode('utf-8')=="<font color=#0000CC><b>Dolu</b></font>":
        msg = msg2
        print "DOLU"
        #os.system(command2)

    if day1.encode('utf-8')!= "<font color=#CC0000><b>Kapalı</b></font>" and day1.encode('utf-8')!="<font color=#0000CC><b>Dolu</b></font>" :
        msg=msg3
        print "AÇILDI"
        os.system(command3)
        server.sendmail(fromadd, toadd1, "RANDEVU AÇILDI")
        print msg
        print  " -AÇILDI- MAIL HAS BEEN SENT "

    server.sendmail(fromadd, toadd2, "CODE WORKING")
    print msg
    print  "REGULAR MAIL HAS BEEN SENT "


    time.sleep(60)


while True:
     getUSD()
