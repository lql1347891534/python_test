from conf.config import ReadConfig
import re
from common.do_excel import DoExcel
from common import logger

class Regnx:

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

    # @staticmethod
    # def replace_access_token(str):
    #     pattern="\$\{(.*?)\}"
    #     access_token=re.search(pattern,str).group(1)
    #     new_access_token=getattr(Context,access_token)
    #     str=re.sub(pattern,new_access_token,str)
    #     return str
           
class Context:
    conf=ReadConfig()
    normal_user=conf.get("login","normal_user")
    pwd=conf.get("login","pwd")

if __name__ == '__main__':
    str=Regnx.replace('{"username":"${normal_user}","password":"${pwd}","verify_code":111,"type":"oa_sc_login"}')
    print(str)