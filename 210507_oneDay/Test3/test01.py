from selenium import webdriver
import unittest
import time
import os
import sys
# 异常处理
from selenium.common.exceptions import NoAlertPresentException

# 必须继承TestCase类
class testCase1(unittest.TestCase):
    # 测试固件 Test Fixture
    # 初始化  self代表testCase1的实例
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        self.driver.get(self.url)
        time.sleep(3)

    # 清理操作
    def tearDown(self):
        self.driver.quit()

    # 方法 以test_开头：默认的去运行
    @unittest.skip("skipping")  # 不执行
    def test_baidu1(self):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys("肖战")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    def test_baidu2(self):
        driver = self.driver
        self.driver.get(self.url)
        # driver.find_element_by_link_text("新闻").click()
        # 判断又没有打开百度页面  ->看title是不是“百度一下你就知道”
        try:
            # 断言
            self.assertEqual(driver.title,"百度一下，就知道",msg="没有打开百度页面")
        # 如果不是，来一个错误截图
        # 创建一个文件夹存放错误截图（driver.get_screenshot_as_file）
        except:
            self.save_error_image(driver,"baidu.png")
        time.sleep(3)

     # self 类的实例
    def save_error_image(self,driver,name):
        if not os.path.exists("./errorImage"):
            os.makedirs("./errorImage")
        # 文件名称         格式化时间
        now = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        driver.get_screenshot_as_file('./errorImage/'+now+"-"+name)


    # 不以test_开头的方法，如果没有调用该方法，则永远不会运行
    def is_alert_exist(self):
        try:
            self.driver.switch_to.alert
        # 没有alert抛异常 返回false
        except NoAlertPresentException as e:
            return False
        return True
    if __name__ == "__main__":
        unittest.main(verbosity=0)


