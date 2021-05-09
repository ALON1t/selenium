from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)
time.sleep(3)
# 用id定位百度搜索框 (全局唯一)
# driver.find_element_by_id("kw").send_keys("迪丽热巴")
# 定位百度一下按钮
# driver.find_element_by_id("su").click()

# 用link-text来定位
# driver.find_element_by_link_text("新闻").click()

# driver.find_element_by_partial_link_text("123").click()

# driver.find_element_by_tag_name("input").send_keys("迪丽热巴")
# driver.find_element_by_tag_name("input").click()

# *省略前面所有的路径
# Copy xpath  （肯定可以定位到这个元素）
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("觉醒年代")
# driver.find_element_by_xpath("//*[@id='su']").click()

# Copy selector
# driver.find_element_by_css_selector("#kw").send_keys("狂人日记")
# driver.find_element_by_css_selector("#su").click()

# time.sleep(5)
# # 清除输入框的内容
# driver.find_element_by_css_selector("#kw").clear()
# driver.find_element_by_css_selector("#kw").send_keys("青春")
# # driver.find_element_by_id("su").click()
#
# # 提交表单
# driver.find_element_by_id("su").submit()

# text 获取文本内容
text = driver.find_element_by_id("s-top-left").text
print(text)
time.sleep(5)
# 关闭浏览器  有清理浏览器的作用
driver.quit()


