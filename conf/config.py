import configparser
from common import constants
import os

# 读取配置文件
class ReadConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        file_name = os.path.join(constants.config_path, "config.txt")
        self.config.read(file_name)

    # 得到str类型
    def get(self,section,option):
        return self.config.get(section,option)
    #  得到int类型
    def getint(self,section,option):
        return self.config.getint(section,option)
    # 得到boolean类型
    def getboolean(self,section,option):
        return self.config.getboolean(section,option)
    # 得到float类型
    def getfloat(self,section,option):
        return self.config.getfloat(section,option)

if __name__ == '__main__':
    conf=ReadConfig().getboolean("switch","on")
    print(conf)
    print(type(conf))