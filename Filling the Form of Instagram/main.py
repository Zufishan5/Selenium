from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Create A Driver 
driver = webdriver.Chrome(options=chrome_options)
# Open a Website
driver.get('https://www.instagram.com/accounts/emailsignup/')
time.sleep(2)
# Let's start filling in forms!
phone_or_email = driver.find_element(By.NAME,'emailOrPhone')
phone_or_email.send_keys('abciaknfdkuhgakns@yahoo.com')
full_name = driver.find_element(By.NAME,'fullName')
full_name.send_keys('Ellie')
username = driver.find_element(By.NAME ,'username')
username.send_keys('futurekajfuhgasjbk')
password = driver.find_element(By.NAME ,'password')
password.send_keys('hellolaihgskbfndvjabsgiuda')
password.submit()