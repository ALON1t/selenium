from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/send.html")
driver.get(file)

driver.find_element_by_tag_name("input").click()
time.sleep(3)
# 得到操作弹框的句柄
alert = driver.switch_to.alert
# 在弹框中输入想输入的数据
alert.send_keys("456ha")
# 关闭
alert.accept()
# alert.dissmiss()  取消

time.sleep(5)
driver.quit()