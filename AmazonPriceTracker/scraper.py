import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import smtplib
import time

ua = UserAgent()

URL = 'https://www.amazon.in/Test-Exclusive-547/dp/B078BNQ318/ref=lp_21439725031_1_1?s=electronics&ie=UTF8&qid=1599626827&sr=1-1'

def check_price():
    page = requests.get(URL, headers={'User-Agent':ua.random})

    soup = BeautifulSoup(page.text, 'lxml')

    title = soup.find(id="productTitle").get_text(strip=True)
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[2:]

    if(converted_price < '40000'):
        send_mail()

    if(converted_price > '40000'):
        send_mail()

    print(title)
    print(converted_price)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('nihalsa1994@gmail.com','fwdwfdightthfmdu')

    subject = 'Price Fell Down!'
    body = 'Check the amazon link https://www.amazon.in/Test-Exclusive-547/dp/B078BNQ318/ref=lp_21439725031_1_1?s=electronics&ie=UTF8&qid=1599626827&sr=1-1 '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'nihalsa1994@gmail.com',
        'nihals.cs18@sahyadri.edu.in',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60)
