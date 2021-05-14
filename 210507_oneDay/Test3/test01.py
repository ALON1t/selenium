# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
import time
import os,sys,csv
from ddt import ddt,file_data,unpack,data
# 异常处理
from selenium.common.exceptions import NoAlertPresentException

def getCsv(file_name):
    pass
    rows = []
    path = sys.path[0]  # 当前文件所在路径
    # 打开文件   rt->读取
    with open(path + '\\' + file_name, 'rt') as f:
        # csv工具  分隔号是逗号
        readers = csv.reader(f, delimiter=',', quotechar='|')
        # 一行一行的读，放到readers里
        next(readers, None)
        # 一行一行的遍历  每一行里面的每个数据放到数组里面
        for row in readers:
            temprows = []
            for i in row:
                # [肖战，肖战_百度搜素]
                temprows.append(i)
            rows.append(temprows)
        return rows


@ddt
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
    # @unittest.skip("skipping")  # 不执行
    # @data("肖战","王一博","腾讯新闻","阿里巴巴")

    # @file_data('test_baidu_data.json')

    @unittest.skip("skipping")
    @data(["肖战","肖战_百度搜索"],["王一博","王一博_百度搜索"],["阿里巴巴","阿里巴巴_百度搜索"])
    @unpack
    def test_baidu1(self,value1,value2):
        driver = self.driver
        driver.get(self.url)
        driver.find_element_by_id("kw").send_keys(value1)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertEqual(driver.title,value2,msg="fail!!!")
        print(driver.title)
        time.sleep(3)

    # @unittest.skip("skipping")
    # def test_baidu11(self):
    #     driver = self.driver
    #     driver.get(self.url)
    #     driver.find_element_by_id("kw").send_keys("Lisa")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(3)

    @data(*getCsv("test_baidu_data.txt"))
    # unpack 一一对应
    @unpack
    def test_baidu3(self, value, expected_value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        print(expected_value)
        print(driver.title)

    @unittest.skip("skipping")
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


