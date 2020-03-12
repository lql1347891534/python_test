import re

s="hell word hello"
pattern1="hello"
s1=re.match(pattern1,s)#match,从起始位置开始找，找不到则返回None
s2=re.findall(pattern1,s)#findall,从起始位置开始找，找到所有匹配的返回，返回类型是列表
s3=re.search(pattern1,s)#search,从起始位置开始找，找到一个匹配的就结束
sr='{"username":"${normal_user}","password":"${pwd}","verify_code":111,"type":"oa_sc_login"}'
pattern="\$\{(.*?)\}"
while re.search(pattern,sr):
    from common.connection import Context
    key=re.search(pattern,sr).group(1)
    new=getattr(Context,key)
    sr=re.sub(pattern,new,sr,count=1)
print(sr)
# sr5=sr4.group()
# sr=sr.replace("${"+re.findall(pattern,sr)[0]+"}","tpacs031")
# sr=sr.replace("${"+re.findall(pattern,sr)[0]+"}","d6cecd8d54b40065ae52cc9116e1d5bc")
