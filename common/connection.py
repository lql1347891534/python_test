from conf.config import ReadConfig
import re
from common.do_excel import DoExcel
from common import logger

class Regnx:
    #利用正则将请求参数里面的token替换
    @staticmethod
    def replace(str):
        pattern="\$\{(.*?)\}"
        while re.search(pattern, str):
            # from common.connection import Context
            key = re.search(pattern, str).group(1)
            new = getattr(Context, key)
            str = re.sub(pattern, new, str, count=1)
            logger.MyLog.info("old_str replace new_str:{0}".format(str))
        return str

#定义类，类名.变量名
class Context:
    conf=ReadConfig()
    normal_user=conf.get("login","normal_user")
    pwd=conf.get("login","pwd")

if __name__ == '__main__':
    str=Regnx.replace('{"username":"${normal_user}","password":"${pwd}","verify_code":111,"type":"oa_sc_login"}')
    print(str)