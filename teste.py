from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By





driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
sleep(5)


product_elements = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_label .inventory_item_name')


print("Segue os três produtos mais vendidos:")
for product_element in product_elements[:3]:
   print(product_element.text)

