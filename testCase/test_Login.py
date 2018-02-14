import requests  
import json 
import unittest
import HTMLTestRunner
import time
import configparser
import csv
import io
import sys
sys.path.append('..\\testFile')
import readConfig

class TestLogin(unittest.TestCase):
	"""docstring for TestLogin"""

	def setUp(self, api):
		readData = readConfig.ReadConfig()
		self.base_url = readData.get_section('HTTP','baseurl') + 'api/auth/postToken'
		print(self.base_url)

	def test_login(self):
		path = '..//testFile//userInfo.csv'
		with open(path, newline='') as f:
			reader = csv.DictReader(f)
			for row in reader:
				self.data = {'lang':'en','fromSys':'scmpcapp','nickname': row['nickname'],'password':row['password']}
				r = requests.post(self.base_url, data=self.data)
				print(r.status_code)
				self.assertEqual(r.status_code,200)
				if self.assertEqual(r.status_code,200):
					# 获取返回的所有数据
					json_data = json.loads(r.text)
					print(json_data["data"]["token"])  #获取返回json数据中的token
					#分段
					# print(r.json())
					#将获取的token写入到config.ini中
					cf = configparser.ConfigParser()
					cf.read('..//testFile//config.ini')
					# cf.add_section('token')    #如果token不存在的话，添加token 
					cf.set('token','token',json_data["data"]["token"])
					cf.write(open('..//testFile//config.ini','w'))	

		
if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(TestLogin("test_login"))
	now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))

	'''#定义个报告存放路径，支持相对路径。
	filename = "..//result//"+now+'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='XX平台V1.0')
	'''
    #普通执行测试用例，无报告B
	runner = unittest.TextTestRunner()
	runner.run(suite)

user01 = TestLogin()