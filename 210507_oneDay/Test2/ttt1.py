# from selenium import webdriver
# import os
# import time
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
#
# file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/level_locate.html")
# driver.get(file)
# # 页面最大化
# driver.maximize_window()
#
# # 层级的定位
#
# driver.find_element_by_link_text("Link1").click()
#
# # 定位下拉列表特定的元素
# ele = driver.find_element_by_id("dropdown1").find_element_by_link_text("Another action")
# time.sleep(3)
# # 把鼠标放到这个元素上，让元素高亮展示
# ActionChains(driver).move_to_element(ele).perform()
#
# time.sleep(5)
# driver.quit()


from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/drop_down.html")
driver.get(file)
# 页面最大化
driver.maximize_window()

# 下拉框处理
time.sleep(3)
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[3]").click()
# driver.find_element_by_css_selector("#ShippingMethod > option:nth-child(3)").click()
options = driver.find_element_by_id("ShippingMethod").find_elements_by_tag_name("option")
# for option in options:
#     if option.get_attribute('value') == '10.69':
#         option.click()

options[2].click()
time.sleep(5)
driver.quit()