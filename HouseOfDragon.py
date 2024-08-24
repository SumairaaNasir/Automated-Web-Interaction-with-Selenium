import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")
box = driver.find_element(By.XPATH,"""//*[@id="APjFqb"]""")
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH,"""//*[@id="kp-wp-tab-overview"]/div[8]/div/div/div/div/div/div[1]/div/div/span/a""").click()
time.sleep(2)
driver.save_screenshot("C:/Users/MY PC/Desktop/New folder.png")