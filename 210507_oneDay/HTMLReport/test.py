# 测试报告

import unittest
from Test3 import test01
from Test3 import test03

import os,sys
import HTMLTestRunner
import time

# 测试套件
def createSuite():

    discover = unittest.defaultTestLoader.discover('../Test3', pattern='test*.py', top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # 获取当前脚本问价所在的文件路径  0-》当前文件所在路径
    curpath = sys.path[0]
    print(curpath)
    # 不存在就创建一个
    if not os.path.exists("/resultReport"):
        os.mkdir(curpath+"/resultReport")
    # 根据时间命名  区分不同文件
    # 格式化时间的函数  time.strftime()
    # 年月日 时分秒  时间戳
    now = time.strftime("%Y-%m-%d-%H %M %S",time.localtime(time.time()))
    filename = curpath+"/resultReport/"+now+"-"+"resultReport.html"
    # 将测试结果写到测试报告里面
    with open(filename,'wb') as fp:
        # title=u"测试报告"  u可以防止乱码 UTF-8
        # verbosity=2  测试用例的详细程度
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"测试用例执行的情况/结果",verbosity=2)
        # 测试套件
        suite = createSuite()
        # 执行
        runner.run(suite)
