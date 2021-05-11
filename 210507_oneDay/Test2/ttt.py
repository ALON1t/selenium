from selenium import webdriver
import os
import time

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/frame.html")
# file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/checkbox.html")
driver.get(file)
# 页面最大化
driver.maximize_window()

# 定位一组元素
# checkbox.html
# driver.find_element_by_id("c1").click()
# driver.find_element_by_id("c2").click()
# driver.find_element_by_id("c3").click()

# inputs = driver.find_elements_by_tag_name("input")
# # 从一组元素中找出type=CheckBox
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()

# frame.html

time.sleep(3)

# 多层框架
# 实现搜索
# # 转换层级
# driver.switch_to_frame("f1")
# driver.switch_to_frame("f2")
#
# driver.find_element_by_id("kw").send_keys("布拉格")
# driver.find_element_by_id("su").click()

# 转换层级
driver.switch_to.frame("f1")
# driver.switch_to_frame("f1") 已经被弃用
driver.switch_to.frame("f2")

driver.find_element_by_id("kw").send_keys("布拉格")
driver.find_element_by_id("su").click()
time.sleep(2)

# 回到默认页面
driver.switch_to.default_content()

driver.switch_to.frame("f1")
driver.find_element_by_link_text("click").click()

time.sleep(5)
driver.quit()
