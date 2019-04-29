import string
import random
import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

'''
1: Get email address
2: Generate normal username
3: ???
'''

passwordlen = 10 #Length of generated passwords

def get_email():
    page = requests.get("https://10minutemail.com/10MinuteMail/index.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[1]
    email = html.find("input", {"class", "mail-address-address"})["value"]
    return email

def generate_password(len):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=len))


email = get_email()
print(email)

driver = webdriver.Chrome()
driver.get("https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2Fr%2Fnews%2F")
driver.find_element_by_id("regEmail").send_keys(email)
driver.find_element_by_class_name("AnimatedForm__nextButton").click()
driver.find_element_by_class_name("Onboarding__usernameSuggestion").click()
password = generate_password(passwordlen)
username = driver.find_element_by_id("regUsername").get_attribute("value")
driver.find_element_by_id("regPassword").send_keys(password)

print(username)

with open("bots.txt", "a+") as f:
    f.write(username + "," + password + "\n")
    f.close()