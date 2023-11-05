from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.pinterest.com/")
sleep(2)
sign_up_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/button/div/div"))
)
sign_up_button.click()
sleep(2)
email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[2]/fieldset/span/div/input"))
)
email_field.send_keys("")
sleep(2)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[4]/fieldset/span/div/input"))
)
password_field.send_keys("spxexepress")

date_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[7]/div/div/div/div/div[1]/span/div/input"))
)
date_input.send_keys("1 1 2000")
sleep(2)
submit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[8]/button/div"))
)
submit_button.click()
sleep(2)

error_message = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div[5]/div/div[1]/form/div[2]/fieldset/span/div[2]/div/span/div/div/div[2]")

if error_message:
    print("An error message was displayed.")
else:
    print("No error message was displayed.")
driver.quit()
