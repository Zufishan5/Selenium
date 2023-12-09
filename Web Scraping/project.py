from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.seleniumeasy.com/')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="node-20"]/div/div/div/div[1]/div/div[2]/p[3]/a[1]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="node-294"]/footer/ul/li/a').click()
time.sleep(2)
header=driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div[1]/h1').text
print("The Header of The Page is :" , header)


