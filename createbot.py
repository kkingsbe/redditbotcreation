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
driver = webdriver.Chrome()

def get_email():
    page = requests.get("https://10minutemail.com/10MinuteMail/index.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    html = list(soup.children)[1]
    email = html.find("input", {"class", "mail-address-address"})["value"]
    return email

def generate_password(len):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=len))

def convert_to_dev(username, password):
    driver.get("https://www.reddit.com/login/")
    driver.find_element_by_id("loginUsername").send_keys(username)
    driver.find_element_by_id("loginPassword").send_keys(password)
    driver.find_element_by_class_name("AnimatedForm__submitButton").click()
    time.sleep(10)
    driver.get("https://www.reddit.com/prefs/apps")
    driver.find_element_by_id("create-app-button").click()
    driver.find_element_by_name("name").send_keys("cow")
    driver.find_element_by_xpath('//*[@id="app_type_script"]').click()
    driver.find_element_by_name("redirect_uri").send_keys("http://www.google.com")
    driver.find_element_by_xpath("/html/body/div[3]/div[2]/form/button").click()
    time.sleep(5)
    secret = driver.find_element_by_class_name('prefright').text
    id = driver.find_element_by_xpath('//*[@id="developed-app-zHGDodMMQ-r0QA"]/div[2]/h3[2]').text
    return secret,id

def register_account():
    email = get_email()
    print(email)
    driver.get("https://www.reddit.com/register/?dest=https%3A%2F%2Fwww.reddit.com%2Fr%2Fnews%2F")
    driver.find_element_by_id("regEmail").send_keys(email)
    driver.find_element_by_class_name("AnimatedForm__nextButton").click()
    driver.find_element_by_class_name("Onboarding__usernameSuggestion").click()
    password = generate_password(passwordlen)
    username = driver.find_element_by_id("regUsername").get_attribute("value")
    driver.find_element_by_id("regPassword").send_keys(password)

    with open("bots.txt", "a+") as f:
        f.write(username + "," + password + "\n")
        f.close()

    input("Press enter once the CAPTCHA is solved so I can create the developer account...")

print(convert_to_dev("IndividualGas1", "testing123"))