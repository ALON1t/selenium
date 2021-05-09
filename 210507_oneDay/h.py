from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()

driver.find_element_by_css_selector("#kw").send_keys("创造营")
driver.find_element_by_css_selector("#su").click()
time.sleep(8)

driver.quit()


