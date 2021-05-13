import unittest
from Test3 import test01
from Test3 import test03

import os,sys
import HTMLTestRunner
import time

# 测试套件
def createSuite():
    suite = unittest.TestSuite()
    # suite.addTest(test01.testCase1("test_baidu1"))
    # suite.addTest(test01.testCase1("test_baidu2"))
    # suite.addTest(test03.testCase2("test_baidu1"))
    # suite.addTest(test03.testCase2("test_baidu2"))

    # 添加所有test_的方法
    # suite.addTest(unittest.makeSuite(test01.testCase1))
    # suite.addTest(unittest.makeSuite(test03.testCase2))

    # TestLoader 还有误
    # suite1 = unittest.TestLoader.loadTestsFromTestCase(test01.testCase1)
    # suite2 = unittest.TestLoader.loadTestsFromTestCase(test03.testCase2)
    # suite.addTest([suite1,suite2])
    # return suite

    discover = unittest.defaultTestLoader.discover('../Test3',pattern='test*.py',top_level_dir=None)
    return discover

if __name__ == "__main__":
    suite = createSuite()
    # TestRunner 执行测试
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)

    # 可以增加verbosity参数，例如unittest.main(verbosity=2)
    # 在主函数中，直接调用main() ，在main中加入verbosity = 2 ，这样测试的结果就会显示的更加详细。
    # 这里的verbosity是一个选项, 表示测试结果的信息复杂度，有三个值:
    # 0(静默模式): 你只能获得总的测试用例数和总的结果比如总共100个，失败20成功80
    # 1(默认模式): 非常类似静默模式只是在每个成功的用例前面有个“.” 每个失败的用例前面有个“F”
    # 2(详细模式): 测试结果会显示每个测试用例的所有相关的信息