import unittest
from common.do_excel import DoExcel
from common import constants
from ddt import ddt,data
from common.request import Request
import json
from common.connection import Context
from common.connection import Regnx
from common import logger

do_excel=DoExcel(constants.testfile_path)
cases=do_excel.get_case("reach")
@ddt
class TestReach(unittest.TestCase):

    def setUp(self) :
        print("测试准备")
    @data(*cases)
    def test_reach(self,case):
        data=Regnx.replace(case.data)
        data=json.loads(data)
        # 判断Context中是否有access_token
        if hasattr(Context,"access_token"):
            access_token=Context.access_token
        else:
            access_token=None
            resq = Request(method=case.method, url=case.url, data=data)
            # print(resq.get_json()["data"]["token"]["access_token"])
            logger.MyLog.info("get access_token from response,access_token:{0}".format(resq.get_json()["data"]["token"]["access_token"]))
            if resq.get_json()["data"]["token"]["access_token"]:
                setattr(Context,"access_token",resq.get_json()["data"]["token"]["access_token"])
                # print(getattr(Context,"access_token"))
                logger.MyLog.info("将access_token添加到Context")
        data=Regnx.replace(case.data)
        data=json.loads(data)
        resq = Request(method=case.method, url=case.url, data=data)
        logger.MyLog.info("发起http请求，请求url:{0}".format(case.url))
        # 断言
        if case.expected=="null":
            expected=json.loads(case.expected)
        else:
            expected=case.expected
        if case.title=="登录成功":
            self.assertEqual(expected,resq.get_json()["msg"])
            logger.MyLog.info("登录接口请求成功  message:{0}".format(resq.get_json()["msg"]))
        else:
            self.assertEqual(expected,resq.get_json()["message"])
            logger.MyLog.info("分案查询接口请求成功 message:{0}".format(resq.get_json()["message"]))

    def tearDown(self) :
        print("测试清除")
