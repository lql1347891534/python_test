import logging
import os
from common import constants
import datetime
import HtmlTestRunnerNew
'''
自定义日志类的步骤：
1、定义一个日志收集器
2、设置输出日志级别
3、设置日志输出格式
4、指定日志输出的渠道
5、将设置的输出渠道添加到日志收集器里面
6、输出日志
'''

# 定义一个日志收集器
logger = logging.getLogger("logs")
# 输出日志级别
logger.setLevel("DEBUG")

def set_handler(levels):
    if levels=="error":
        logger.addHandler(MyLog.error_handler)
    else:
        logger.addHandler(MyLog.handler)
    logger.addHandler(MyLog.ch)
    logger.addHandler(MyLog.report_handler)

def remove_handler(levels):
    if levels=="error":
        logger.removeHandler(MyLog.error_handler)
    else:
        logger.removeHandler(MyLog.handler)
    logger.removeHandler(MyLog.ch)
    logger.removeHandler(MyLog.report_handler)

# 获取当天的日志存放目录
def get_log_dir():
    log_dir=os.path.join(constants.logs_path,get_current_day())
    if not os.path.isdir(log_dir):#判断是否存在
        os.makedirs(log_dir)#不存在就创建
    return log_dir#存在就直接返回

# 获取系统当天的日期
def get_current_day():
    return datetime.datetime.now().strftime("%Y%m%d")

class MyLog:
    log_dir=get_log_dir()
    log_file=os.path.join(log_dir,"logs.txt")#定义"INFO"级别日志输出的文件目录
    error_file=os.path.join(constants.logs_path,"error.txt")
    # 设置日志输出的格式
    formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    # 指定输出渠道
    # 控制台输出
    ch=logging.StreamHandler()
    ch.setLevel("DEBUG")#DEBUG级别的日志打印到控制台
    ch.setFormatter(formatter)#添加控制台日志输出的格式

    # INFO文件输出
    handler=logging.FileHandler(filename=log_file,encoding='utf-8')
    handler.setLevel("INFO")
    handler.setFormatter(formatter)

    # ERROR文件输出
    error_handler=logging.FileHandler(filename=error_file,encoding='utf-8')
    error_handler.setLevel("ERROR")
    error_handler.setFormatter(formatter)

    #测试报告日志输出
    report_handler=logging.StreamHandler(HtmlTestRunnerNew.stdout_redirector)
    report_handler.setLevel("INFO")
    report_handler.setFormatter(formatter)

    @staticmethod
    def debug(msg):
        set_handler('debug')
        logger.debug(msg)
        remove_handler('debug')

    @staticmethod
    def info(msg):
        set_handler('info')
        logger.info(msg)
        remove_handler('info')

    @staticmethod
    def error(msg):
        set_handler('error')
        logger.error(msg)
        remove_handler('error')
