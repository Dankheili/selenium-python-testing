from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
import time

chrome_driver_path = "G:/Data/Web Drivers/chromedriver-win64-147/chromedriver.exe"
service = Service(chrome_driver_path, log_path=r"G:\Data\GitHub\selenium-python-testing\chromedriver.log")
driver = webdriver.Chrome(service=service, options=options)
demo_website = "file:C://Users//TestAdmin//Documents//Selenium Python Automation Course//01 Automate Finding Elements 01//01 Source Files//01 demo-website.html"

driver.get(demo_website)
driver.maximize_window()
input_field = driver.find_element(by="id", value="demo-submission-id") # - Finding element by id attribute
#input_field = driver.find_element(by="name", value="demo-submission-name") - Finding element by name attribute
input_field.send_keys("Dankheili")
time.sleep(2)
input_field.submit()
time.sleep(5)
driver.close()