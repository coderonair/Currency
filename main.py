# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime
from notify_run import Notify
import os


import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate



def getUSD():
    # specify the url
    quote_page = "https://kur.doviz.com/serbest-piyasa"

    # query the website and return the html to the variable page
    page = urllib2.urlopen(quote_page)

    # parse the html using beautiful soup and store in variable soup
    soup = BeautifulSoup(page, "html.parser")

    # Take out the <div> of name and get its value
    name_box = soup.find_all("span", attrs={"class": "menu-row2"})

    value = name_box[1].text.strip() # strip() is used to remove starting and trailing
    value =value.replace(',', '.')
    print  datetime.now()
    print  "  USD: " + value

    # open a csv file with append, so old data will not be erased
    with open("index.csv", "a") as csv_file:
     writer = csv.writer(csv_file)
     writer.writerow([value, datetime.now()])

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #Next, log in to the server
    server.login("afpsoft", "anahtaranahtar")

    #Send the mail
    msg = "USD  " + str(value)
    fromadd="afpsoft@gmail.com"
    toadd="afpsoft@gmail.com"
    server.sendmail(fromadd, toadd, msg)
    print msg
    print  " MAIL HAS BEEN SENT "

    # notify = Notify()
    # notify.send(msg)

    msg1 = "5-1 alti USD:  " + str(value)
    msg2 = "5-1 ustu USD:  " + str(value)
    command1 ="curl https://notify.run/pwIkd1EewIG3SpTy -d " + "\"" + msg1 + "\""
    command2 ="curl https://notify.run/pwIkd1EewIG3SpTy -d " + "\"" + msg2 + "\""
    # print command1
    # print command2
    # print value
    # if float(value)<5.1000:
    #     print "case1"
    #     os.system(command1)

    if float(value)>=5.1000:
        print "case2"
        os.system(command2)

    time.sleep(608)


while True:
     getUSD()
