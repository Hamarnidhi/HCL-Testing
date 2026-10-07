from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

try:
    # TC06: Double Click
    driver.get("https://demoqa.com/buttons")
    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()
    print("TC06 Passed: Double-clicked button.")

    # TC07: Drag & Drop
    driver.get("https://demoqa.com/droppable")
    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    actions.drag_and_drop(source, target).perform()
    print("TC07 Passed: Dragged and dropped element.")

    # TC08: Explicit Wait (Visibility)
    driver.get("https://demoqa.com/dynamic-properties")
    visible_btn = wait.until(
        EC.visibility_of_element_located((By.ID, "visibleAfter"))
    )
    print(f"TC08 Passed: Element loaded and visible -> {visible_btn.text}")

    # TC09: Clickable Wait
    driver.get("https://demoqa.com/dynamic-properties")
    enable_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "enableAfter"))
    )
    enable_btn.click()
    print("TC09 Passed: Button became clickable and was clicked.")

    # TC10: Alert Wait
    driver.get("https://demoqa.com/alerts")
    driver.find_element(By.ID, "timerAlertButton").click()
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("TC10 Passed: Alert appeared and was accepted.")

finally:
    driver.quit()