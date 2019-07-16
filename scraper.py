import requests
from bs4 import BeautifulSoup
import smtplib
import time
#This is just a seperate file with my email, username, and password credentials 
import credentials

URL = "https://www.amazon.com/gp/product/B00PFXI9I2/ref=ox_sc_saved_title_2?smid=ATVPDKIKX0DER&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/73.0.3683.75 Safari/537.36"
}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "lxml")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if (converted_price < 10.00):
        send_mail()

    print(title.strip())
    print(converted_price)


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(Username, pw)

    subject = "The Price Fell Down!"
    body = "Check the Amazon link https://www.amazon.com/gp/product/B00PFXI9I2/ref=ox_sc_saved_title_2?smid=ATVPDKIKX0DER&psc=1"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        Username,
        pw2,
        msg
    )

    print("The message has been sent :)")

    server.quit()


while(True):
    check_price()
    time.sleep(86400)
