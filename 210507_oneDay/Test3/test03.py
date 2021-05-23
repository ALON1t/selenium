from selenium import webdriver
import unittest
import time
# 异常处理
from selenium.common.exceptions import NoAlertPresentException

# 必须继承TestCase类
class testCase2(unittest.TestCase):
    # 测试固件 Test Fixture
    # 任何继承自unittest.TestCase的两个固定方法
    #  def setUp(self) 初始化    def tearDown(self)清理工作
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

    # TestCase
    # test_ 运行这个类的时候默认执行

    # 测试套件（存放测试用例【测试方法】的一个容器）  运行测试套件 所有的测试用例都可以运行
    # addTest  可以一次存放一个测试脚本里一个类的一个方法（必须提供方法名）
    # makeSuite 可以一次存放一个测试脚本的一个类的所有方法
    # TestLoader  可以一次存放一个测试脚本的一个类的所有方法
    # discover 可以把指定文件夹下所有特定格式命名的测试脚本中类的所有以test_开头的所有方法

    # runner
    # # 测试套件
    #  suite = createSuite()
    # # 执行
    #  runner.run(suite)

    # unittest框架中测试用例的执行顺序 ： 0-9 A-Z a-z
    # unittest是python的单元测试框架
    # Java的单元测试框架是白盒的
    # 白盒测试的单元测试框架是junit

    # 忽略测试用例的执行  @unittest.skip("skipping")

    # 断言
    # 1 assertEqual(arg1, arg2, msg=None) 验证arg1=arg2，不等则fail
    # 2 assertNotEqual(arg1, arg2, msg=None) 验证arg1 != arg2, 相等则fail
    # 3 assertTrue(expr, msg=None) 验证expr是true，如果为false，则fail
    # 4 assertFalse(expr,msg=None) 验证expr是false，如果为true，则fail

    # 测试报告
    # # 需要有HTMLTestRunner.py 文件  放到C:\Users\LENOVO\AppData\Local\Programs\Python\Python38\Lib 路径下
    # 见HTMLReport

    # 错误截图   保存错误截图driver.get_screenshot_as_file()
    #
    #     def test_baidu2(self):
    #         driver = self.driver
    #         self.driver.get(self.url)
    #         # driver.find_element_by_link_text("新闻").click()
    #         # 判断有没有打开百度页面  ->看title是不是“百度一下你就知道”
    #         try:
    #             # 断言
    #             self.assertEqual(driver.title,"百度一下，就知道",msg="没有打开百度页面")
    #         # 如果不是，来一个错误截图
    #         # 创建一个文件夹存放错误截图（driver.get_screenshot_as_file）
    #         except:
    #             # 调用
    #             self.save_error_image(driver,"baidu.png")
    #         time.sleep(3)
    #
    #      # self 类的实例
    #     def save_error_image(self,driver,name):
    #         if not os.path.exists("./errorImage"): # 看有没有这个文件
    #             os.makedirs("./errorImage")
    #         # 文件名称         格式化时间
    #         now = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
    #         driver.get_screenshot_as_file('./errorImage/'+now+"-"+name)

    # 数据驱动  用数据来驱动测试方法的执行
    # 需要安装ddt  打开cmd pip show ddt 看是否有安装ddt,出现版本号即有安装，若未安装，输入指令pip install ddt安装
    # 使用ddt  导包 from ddt import ddt,file_data,unpack,data
    # 在类前面写上@ddt   见test01.py
    #  如：@ddt
    #     # 必须继承TestCase类
    #     class testCase1(unittest.TestCase)
    #  @data(["肖战","肖战_百度搜索"],["王一博","王一博_百度搜索"],["阿里巴巴","阿里巴巴_百度搜索"])  四个数据分别执行一次，驱动四次这个方法，每次使用不同的参数执行这个方法
    #     也可以将所有需要测试的数据放入json文件 --》 @file_data('test_baidu_data.json')
    #  @unpack  传入的数据是数组或列表时使用unpack
    #    如： @data(["肖战","肖战_百度搜索"],["王一博","王一博_百度搜索"],["阿里巴巴","阿里巴巴_百度搜索"])
    #         @unpack
    #         def test_baidu1(self,value1,value2):
    #         driver = self.driver
    #         driver.get(self.url)
    #         driver.find_element_by_id("kw").send_keys(value1)
    #         driver.find_element_by_id("su").click()
    #         time.sleep(3)
    #         self.assertEqual(driver.title,value2,msg="fail!!!")
    #         print(driver.title)
    #         time.sleep(3)

    #   还可以从一个txt文件读取
    #   需要定义一个专门读取该文件的函数
    #     如：def getCsv(file_name):
    #     pass
    #     rows = []
    #     path = sys.path[0]  # 当前文件所在路径
    #     # 打开文件   rt->读取
    #     with open(path + '\\' + file_name, 'rt') as f:
    #         # csv工具  分隔号是逗号
    #         readers = csv.reader(f, delimiter=',', quotechar='|')
    #         # 一行一行的读，放到readers里
    #         next(readers, None)
    #         # 一行一行的遍历  每一行里面的每个数据放到数组里面
    #         for row in readers:
    #             temprows = []
    #             for i in row:
    #                 # [肖战，肖战_百度搜素]
    #                 temprows.append(i)
    #             rows.append(temprows)
    #         return rows
    # 如： @data(*getCsv("test_baidu_data.txt"))
    #     # unpack 一一对应
    #     @unpack
    #     def test_baidu3(self, value, expected_value):
    #         driver = self.driver
    #         driver.get(self.base_url + "/")
    #         driver.find_element_by_id("kw").clear()
    #         driver.find_element_by_id("kw").send_keys(value)
    #         driver.find_element_by_id("su").click()
    #         time.sleep(3)
    #         print(expected_value)
    #         print(driver.title)