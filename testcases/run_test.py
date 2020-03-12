import unittest
from testcases import test_login
from common import constants
import HtmlTestRunnerNew
import os
from testcases import test_reach

# 实例化一个测试套件
suit=unittest.TestSuite()
# 实例化加载测试用例
loader=unittest.TestLoader()
# # 加载测试用例   loaderTestSFromModule表示执行整个测试模块儿的测试用例
# suit.addTest(loader.loadTestsFromModule(test_reach))

# discover一次性执行所有的测试用例
discover=unittest.defaultTestLoader.discover(constants.testcase_path,"test*.py")
suit.addTest(discover)

test_report_file=os.path.join(constants.reports_path,"test_reports.html")
with open(test_report_file,mode="wb+") as file:
    #执行测试用例
    runner=HtmlTestRunnerNew.HTMLTestRunner(stream=file,title="api_test report")
    runner.run(suit)



