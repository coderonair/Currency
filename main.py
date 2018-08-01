# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

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
    msg = "USD" + str(value)
    fromadd="afpsoft@gmail.com"
    toadd="afpsoft@gmail.com"
    server.sendmail(fromadd, toadd, msg)
    print  " MAIL HASS BEEN SENT "
    time.sleep(1800)



while True:
     getUSD()
