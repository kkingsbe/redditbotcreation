import requests
from bs4 import BeautifulSoup

def get_email():
    page = requests.get("https://10minutemail.com/10MinuteMail/index.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[1]
    email = html.find("input", {"class", "mail-address-address"})["value"]
    return email
