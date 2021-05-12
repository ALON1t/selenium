from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/modal.html")
driver.get(file)
time.sleep(3)

driver.find_element_by_link_text("Click").click()
# driver.find_element_by_id("show_modal").click()
time.sleep(3)
# 点击Click后出现的弹框
# 先定位到div里面
div0 = driver.find_element_by_class_name("modal-body")
div0.find_element_by_id("click").click()
time.sleep(3)

# 在出现的弹框中，点击click me后的弹框
div1 = driver.find_element_by_class_name("modal-footer")
# div1.find_element_by_class_name("btn").click()

buttons = div1.find_elements_by_tag_name("button")
buttons[0].click()

time.sleep(5)
driver.quit()