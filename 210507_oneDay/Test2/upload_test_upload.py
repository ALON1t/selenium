from selenium import webdriver
import os
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

file = "file:///" + os.path.abspath("C:/Users/LENOVO/Desktop/selenium2html/upload.html")
driver.get(file)
time.sleep(3)

# 文件上传操作
driver.find_element_by_tag_name('input').send_keys("C:/Users/LENOVO/Pictures/Saved Pictures/QQ图片20210413135025.jpg")

time.sleep(5)
driver.quit()