from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://learner.saveetha.in/academics/people_schedule/")
driver.maximize_window()

regno = driver.find_element(By.ID, "id_username")
regno.send_keys("23014399")

password = driver.find_element(By.ID, "id_password")
password.send_keys("4343")

time.sleep(3)
submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()

input()