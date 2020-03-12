import requests
from common import logger

class Request:

    #
    def __init__(self,method,url,data=None,cookies=None,headers=None):
        try:
            if method=="get":
                self.resq=requests.get(url=url,params=data,cookies=cookies,headers=headers)
                logger.MyLog.info("use get request")
            elif method=="post":
                self.resq = requests.post(url=url, data=data, cookies=cookies, headers=headers)
                logger.MyLog.info("use post request")
            elif method=="options":
                self.resq = requests.options(url=url, params=data, cookies=cookies, headers=headers)
                logger.MyLog.info("use options request")
            elif method=="head":
                self.resq = requests.head(url=url, params=data, cookies=cookies, headers=headers)
                logger.MyLog.info("use head request")
            elif method=="patch":
                self.resq = requests.patch(url=url, params=data, cookies=cookies, headers=headers)
                logger.MyLog.info("use patch request")
            else:
                self.resq = requests.delete(url=url, params=data, cookies=cookies, headers=headers)
                logger.MyLog.info("use delete request")
        except Exception as a:
            logger.MyLog.error("request was aborted")
            raise a

    #获取状态码
    def get_status_code(self):
        logger.MyLog.info("Get status code from response")
        return self.resq.status_code

    #获取text格式的返回值
    def get_text(self):
        logger.MyLog.info("Get text from response")
        return self.resq.text

    # 获取json格式的返回值
    def get_json(self):
        logger.MyLog.info("Get json from response")
        return self.resq.json()