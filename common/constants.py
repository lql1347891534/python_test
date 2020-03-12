import os

# 获取当前文件的根目录
base_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_path=os.path.join(base_path,"conf")

testdata_path=os.path.join(base_path,"datas")
testfile_path=os.path.join(testdata_path,"test_data.xlsx")

testcase_path=os.path.join(base_path,"testcases")

logs_path=os.path.join(base_path,"logs")

reports_path=os.path.join(base_path,"reports")