import requests
import smtplib
import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
email_id = os.getenv("EMAIL_ID")
password = os.getenv("APP_PASSWORD")
BUY_PRICE = os.getenv("BUY_PRICE")

header = {
    "User-Agent": "Mozilla/5.0 ()",
    "Accept-Language": "en-GB, en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header, verify=False)

with open('file.txt', 'w') as file:
    file.write(str(response.content))

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()

print(price)

price_as_list = list(price)
price_as_list.pop(0)
res = []
for char in price_as_list:
    if char != ',':
        res.append(char)
price_as_string = "".join(res)
price_as_float = float(price_as_string)

print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

print(float(BUY_PRICE))

if price_as_float < float(BUY_PRICE):
    # send an Email alert
    message = f"{title} is now available in {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            result = connection.login(email_id, password)
            print(result)
            connection.sendmail(
                from_addr=email_id,
                to_addrs=email_id,
                msg = f"Subject:Amazon price alert!\n\n{message}\n{URL}".encode("utf-8")
            )

