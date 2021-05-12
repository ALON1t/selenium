from selenium import webdriver
import unittest
import time
# 异常处理
from selenium.common.exceptions import NoAlertPresentException

# 必须继承TestCase类
class testCase1(unittest.TestCase):
    # 测试固件
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
    def test_baidu1(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("肖战")
        driver.find_element_by_id("su").click()
        time.sleep(3)

    def test_baidu2(self):
        driver = self.driver
        driver.find_element_by_link_text("新闻").click()
        time.sleep(3)

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


