#_*_conding:utf-8_*_
#@Time    :2020/2/1815:36
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com

import unittest
import os
from datetime import datetime
from Libs.HTMLTestRunnerNew import HTMLTestRunner
from Common.dir_config import *

#实例化套件对象
suite = unittest.TestSuite()

#TestLoader的用法
#1、实例化TestLoader对象
#2、使用discover去找到一个目录下的所有测试用例
loader = unittest.TestLoader()
suite.addTests(loader.discover(testcases_dir))
#测试报告的保存路径及文件格式
report_name = "WebAutoTest_" + datetime.strftime(datetime.now(),"%Y%m%d%H%M%S") + ".HTML"
report_path = os.path.join(htmlreport_dir,report_name)

#执行测试用例
with open(report_path, 'wb') as fp:
    runner = HTMLTestRunner(
            stream=fp,
            title='单元测试报告',
            description='Web自动化测试报告',
            tester="八两"
            )
    runner.run(suite)