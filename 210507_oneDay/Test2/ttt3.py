from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/alert.html")
driver.get(file)
# 页面最大化
# driver.maximize_window()

driver.find_element_by_id("tooltip").click()

# 关闭弹框
# 得到了操作弹框的句柄
alert = driver.switch_to.alert
# 关闭
alert.accept()

time.sleep(5)
driver.quit()

