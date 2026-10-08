from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")

name = driver.find_element(By.XPATH, "//input[@id='name']")
name.click()
name.send_keys("HAMAR")

email = driver.find_element(By.XPATH, "//input[@id='email']")
email.send_keys("hamarnidhi@gmail.com")

number = driver.find_element(By.XPATH, "//input[@id='mobile']")
number.send_keys("8778940671")

male = driver.find_element(By.XPATH, "//input[@id='gender' and @type='radio']")
male.click()

dob = driver.find_element(By.XPATH, "//input[@id='dob']")
dob.send_keys("09032006")

sub = driver.find_element(By.XPATH, "//input[@name ='subjects']")
sub.send_keys("PYTHON TRAINING")

# hob = driver.find_element(By.XPATH, "//input[@id='hobbies']").click()

# address = driver.find_element(By.XPATH, "//textarea[@id='address']").click()
# address.send_keys("Saveetha Engineering College, Thandalam, Chennai - 600054")

# state = driver.find_element(By.XPATH, "//input[@id = 'state' and value='Rajasthan']").click()

city = driver.find_element(By.XPATH, "//input[@id='city' and value='agra']").click()
input()