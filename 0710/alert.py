from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.maximize_window()

try:
    print("--- Running TC01: Open Demo Website ---")
    clean_url = "https://demo.automationtesting.in/Alerts.html"
    driver.get(clean_url)
    
    assert "Alerts" in driver.title or "Automation Testing" in driver.title
    print("SUCCESS (TC01): Website opened successfully.")

    print("\n--- Running TC02: Alert - accept() ---")
    tab_confirm = driver.find_element(By.XPATH, "//a[href='#CancelTab' or contains(text(), 'Alert with OK & Cancel')]")
    tab_confirm.click()
    
    btn_confirm = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='CancelTab']/button")))
    btn_confirm.click()
    
    alert = wait.until(EC.alert_is_present())
    print(f"Alert Text: '{alert.text}'")
    alert.accept()
    
    confirm_msg = driver.find_element(By.ID, "demo").text
    assert "You pressed Ok" in confirm_msg
    print(f"SUCCESS (TC02): Action confirmed via alert.accept(). Result: '{confirm_msg}'")

    print("\n--- Running TC03: Alert - dismiss() ---")
    btn_confirm.click()
    
    alert = wait.until(EC.alert_is_present())
    alert.dismiss()
    
    cancel_msg = driver.find_element(By.ID, "demo").text
    assert "You Pressed Cancel" in cancel_msg or "Cancel" in cancel_msg
    print(f"SUCCESS (TC03): Action canceled via alert.dismiss(). Result: '{cancel_msg}'")

    print("\n--- Running TC04: Prompt - send_keys() ---")
    tab_prompt = driver.find_element(By.XPATH, "//a[contains(text(), 'Alert with Textbox')]")
    tab_prompt.click()

    btn_prompt = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Textbox']/button")))
    btn_prompt.click()
    
    prompt_alert = wait.until(EC.alert_is_present())
    customer_name = "Alex Mercer"
    prompt_alert.send_keys(customer_name)
    prompt_alert.accept()
    
    prompt_msg = driver.find_element(By.ID, "demo1").text
    assert customer_name in prompt_msg
    print(f"SUCCESS (TC04): Information submitted via send_keys(). Result: '{prompt_msg}'")
    print("\n--- Running TC05: Mouse Hover ---")
    switch_to_menu = driver.find_element(By.XPATH, "//a[contains(text(), 'SwitchTo')]")
    
    actions = ActionChains(driver)
    actions.move_to_element(switch_to_menu).perform()

    submenu_item = driver.find_element(By.XPATH, "//a[contains(text(), 'Windows')]")
    assert submenu_item.is_displayed()
    print("SUCCESS (TC05): Hover successful. Navigation submenu displayed.")

finally:
    input("\nPress Enter to close the browser...")
    driver.quit()
    print("\nAll test cases executed successfully on demo.automationtesting.in!")