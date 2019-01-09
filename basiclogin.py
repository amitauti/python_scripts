from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_value = "amitauti.work"
password_value = "<your password goes here>"

browser = webdriver.Chrome(executable_path=r'C:/chromedriver_win32/chromedriver.exe')

browser.get("https://accounts.google.com/signin/v2/identifier?hl=en&passive=true&continue=https%3A%2F%2Fwww.google.com%2F%3Fgws_rd%3Dssl&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
print ("Google opened")
sleep(10)

browser.find_element_by_id("identifierId").send_keys(user_value)
browser.find_element_by_id("identifierNext").click()
print ("username entered")
sleep (10)

browser.find_element_by_name("password").send_keys(password_value)
browser.find_element_by_id("passwordNext").click()
print ("password entered")
sleep (10)

browser.quit()
