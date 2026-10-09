
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://assertqa.com/practice/webtables")

print("TC01 - Column Headings")
headings = driver.find_elements(By.XPATH, "//th")
for heading in headings:
    print(heading.text)

print("TC02 - First Data Row")
rows = driver.find_elements(By.XPATH, "//tbody/tr")
print(rows[0].text)

print("TC03 - Last Data Row")
rows = driver.find_elements(By.XPATH, "//tbody/tr")
print(rows[-1].text)

print("TC04 - Search by Last Name")
search = driver.find_element(By.XPATH, "//input[@placeholder='Search by name, email...']")
search.send_keys("Johnson")
rows = driver.find_elements(By.XPATH, "//tbody/tr")
for row in rows:
    print(row.text)

print("TC05 - Email Addresses")
emails = driver.find_elements(By.XPATH, "//tbody/tr/td[4]")
for email in emails:
    print(email.text)

print("TC06 - Highest Salary")
rows = driver.find_elements(By.XPATH, "//tbody/tr")
highest_salary = 0
highest_employee = ""

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")

    first_name = cells[1].text
    last_name = cells[2].text
    salary = int(cells[5].text.replace("$", "").replace(",", ""))

    if salary > highest_salary:
        highest_salary = salary
        highest_employee = first_name + " " + last_name
print("Salary:", highest_salary)

print("TC07 - Check Link")
links = driver.find_elements(By.XPATH, "//a[@href='https://assertqa.com/practice/webtables']")

if len(links) > 0:
    print("PASS - Link exists")
else:
    print("FAIL - Link does not exist")

print("TC08 - Count Rows")
rows = driver.find_elements(By.XPATH, "//tbody/tr")
print("Total rows:", len(rows))

input()
driver.quit()
