import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.find_element(By.XPATH,"//a[contains(@aria-label,'Google apps')]").click()
time.sleep(10)
#Somthing
#Branching   This is to check the changes in master from branch
#Testing
#Otherthing
#Nothing
driver.find_element(By.XPATH,"//span[@data-text='YouTube']").click()