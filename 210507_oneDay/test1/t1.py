from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(3)
driver.get("http://127.0.0.1:88/zentao/user-login.html")
time.sleep(3)
# 用name来定位
driver.find_element_by_name("account").send_keys("admin")
time.sleep(3)
driver.find_element_by_name("password").send_keys("pAPe478I8vz")
time.sleep(3)
driver.find_element_by_id("submit").click()
time.sleep(5)
driver.quit()
