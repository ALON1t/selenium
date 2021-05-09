from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:88/zentao/user-login.html")
driver.maximize_window()

# 登录
account = driver.find_element_by_name("account")
account.send_keys("admin")
# 模拟Tab键
account.send_keys(Keys.TAB)
time.sleep(5)
password = driver.find_element_by_name("password")
password.send_keys("pAPe478I8vz")
password.send_keys(Keys.ENTER)

# driver.find_element_by_name("account").send_keys("admin")
# password = driver.find_element_by_name("password")
# password.send_keys("pAPe478I8vz")
# password.send_keys(Keys.ENTER)

# driver.find_element_by_name("account").send_keys("admin")
# driver.find_element_by_name("password").send_keys("pAPe478I8vz")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)

# driver.find_element_by_id("submit").click()

time.sleep(5)
driver.quit()

