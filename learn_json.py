import json

# 序列化，将dict序列化成str或者file  dumps(dict) dump(file)
dict_obj={"msg":"用户名密码错误","rc":1,"data":None}
str=json.dumps(dict_obj,ensure_ascii=False)
# print(str)
# print(type(str))

# 反序列化， 将str或者file反序列化成dict loads(str)  load(file)
str_test='{"msg":"用户名密码错误","rc":1,"data":null}'
# str_test2='{"a":[1,2],"b":["c","d"]}'
# dict=json.loads(str_test2)
# print(dict)
# print(type(dict))

# 将文件中的str反序列化成dict
f=open(r"D:\Python_test\datas\data.json")
s=json.load(f)
print(s)
print(type(s))

# 将dict序列化写入文件
f=open(r"D:\Python_test\datas\data.json","w+")
dict_obj1={"msg":"aaa","rc":1,"data":None}
s=json.dump(dict_obj1,f)

