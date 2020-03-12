import unittest
from common.request import Request
from common.do_excel import DoExcel
from common import constants
import json
from ddt import ddt,data,unpack

do_excel = DoExcel(constants.testfile_path)
cases = do_excel.get_case("login")
@ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        print("测试准备")

    @data(*cases)
    def test_login(self,case):
        data=json.loads(case.data)
        resq=Request(method=case.method,url=case.url,data=data)
        print(resq.get_json())
        if case.expected == "null":
            expected=json.loads(case.expected)
        else:
            expected=case.expected
            #断言
        self.assertEqual(expected,resq.get_json()["msg"])
        print("成功")

    def tearDown(self):
        print("测试清除")