import urllib.request
import urllib.parse
import requests  
import json 

# params = urllib.parse.urlencode({'username': 'plat_yxj','password':'123456'})
# url = "http://scmbase.loongjoy.com/api/auth/postToken?%s" % params
# with urllib.request.urlopen(url) as f:
# 	print(f.read().decode('utf-8'))

#python标准库

# DATA = urllib.parse.urlencode({'nickname': 'plat_yxj','password':'123456','fromSys':'scmpcapp','lang':'zh'}).encode('utf-8')
# req = urllib.request.Request(url='http://scmbase.loongjoy.com/api/auth/postToken', data=DATA,method='POST')
# with urllib.request.urlopen(req) as f:
#     pass

# print(f.status)
# print(f.reason)



url = 'http://scmbase.loongjoy.com/api/auth/postToken'
data = {'nickname': 'plat06','password':'123456','fromSys':'scmpcapp','lang':'zh'}
r = requests.post(url, data=data)  
r = requests.post(url, data=data)  
# 获取 接口返回的数据信息并解析（如果返回的是json格式的话）  
json_data = json.loads(r.text)  
print(json_data)



