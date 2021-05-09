from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 浏览器的最大化
# driver.maximize_window()

driver.find_element_by_id("kw").send_keys("肖战")
driver.find_element_by_id("su").submit()
# 固定等待
time.sleep(5)
# move_to_element() 移动
tr = driver.find_element_by_link_text("肖战杨紫横店聚餐")
ActionChains(driver).move_to_element(tr).perform()

time.sleep(5)
title = driver.title
url = driver.current_url
print(title)
print(url)
time.sleep(5)

kw = driver.find_element_by_id("kw")


time.sleep(5)
driver.quit()