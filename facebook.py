from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:\Users\sheah\OneDrive\Desktop\python\chromedriver.exe",chrome_options=options)

url = 'https://facebook.com'

driver.get(url)

username =driver.find_element(By.ID, "email")
username.send_keys('sheahead22@gmail.com')
password =driver.find_element(By.ID, "pass")
password.send_keys('Your Password')
login =driver.find_element(By.NAME, "login")
login.click()

...

