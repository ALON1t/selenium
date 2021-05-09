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

# 智能等待
# driver.implicitly_wait(10)
# driver.find_element_by_link_text("肖战(中国内地男演员、歌手) - 百度百科").click()

title = driver.title
url = driver.current_url
print(title)
print(url)
time.sleep(5)
# # 设置浏览器的宽度 高度
# driver.set_window_size(480,800)

# # 浏览器的后退
# driver.back()
# time.sleep(5)
# # 浏览器的前进
# driver.forward()

# 浏览器控制条的下拉  拉到底端
# ScrollTop=10000
# js1 = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js1)
# time.sleep(5)
# # 浏览器控制条拉到顶端
# js2 = "var q=document.documentElement.scrollTop=0"
# driver.execute_script(js2)

kw = driver.find_element_by_id("kw")
# 键盘组合键的用法
# Ctrl A  Ctrl C
# kw.send_keys(Keys.CONTROL,'a')
# kw.send_keys(Keys.CONTROL,'x')
# time.sleep(5)
# kw.send_keys("杨紫")
# su = driver.find_element_by_id("su")

# 右击
# perform() 执行
# ActionChains(driver).context_click(su).perform()

# 双击
# ActionChains(driver).double_click(su).perform()

# drag_and_drop() 拖动
# move_to_element() 移动  见t4.py


# driver.find_element_by_id("su").submit()

time.sleep(5)
driver.quit()