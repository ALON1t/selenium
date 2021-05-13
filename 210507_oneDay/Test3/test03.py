from selenium import webdriver
import unittest
import time
# 异常处理
from selenium.common.exceptions import NoAlertPresentException

# 必须继承TestCase类
class testCase2(unittest.TestCase):
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
    def test_baidu1(self):
        driver = self.driver
        driver.find_element_by_id("kw").send_keys("王一博")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        print(driver.title)

        # 断言
        # self.assertEqual(driver.title,"王一博_百度搜索",msg="not equal!")
        # self.assertNotEqual(driver.title, "百度搜索", msg="not equal!")
        self.assertTrue(1!=2,msg="not equal!")  # 运行错误

    # 忽略用例的执行   @unittest.skip("skipping")
    @unittest.skip("skipping")
    def test_baidu2(self):
        driver = self.driver
        driver.find_element_by_link_text("hao123").click()
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
        unittest.main(verbosity=1)
