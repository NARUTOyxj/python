import requests  
import json 
import unittest
import HTMLTestRunner
import time
import configparser
import csv
import io

class TestLogin(unittest.TestCase):
	"""docstring for TestLogin"""

	def setUp(self):
		self.base_url = 'http://scmbase.loongjoy.com/api/auth/postToken'

	def test_login(self):
		path = 'D:/SCM/python/testFile/userInfo.csv'
		with open(path, newline='') as f:
			reader = csv.DictReader(f)
			for row in reader:
				nickname = row['nickname']
				password = row['password']
				status = int(row['result'])
				self.data = {'lang':'en','fromSys':'scmpcapp','nickname': nickname,'password':password}
				r = requests.post(self.base_url, data=self.data)
				json_data = json.loads(r.text)
				r_status = json_data['status']
				print(r_status)
				self.assertEqual(r_status,status)
				if r_status == 0:
					getToken = json_data['data']['token']  #获取返回json数据中的token
					#将获取的token写入到config.ini中
					cf = configparser.ConfigParser()
					cf.read('D:/SCM/python/testFile/config.ini')
					# cf.add_section('token')    #如果token不存在的话，添加token 
					cf.set('token','token',getToken)
					cf.write(open('D:/SCM/python/testFile/config.ini','w'))
				else:
					print('data wrong')	

		
if __name__ == '__main__':
	# 加载测试用例
	suite = unittest.TestSuite()
	suite.addTest(TestLogin("test_login"))

	'''
	# 定义个报告存放路径，支持相对路径。
	now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
	filename = "D:/SCM/python/result/"+now+'result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='自动化测试报告', description='SCM2.0测试系统 V1.0')
	'''
    #普通执行测试用例，无报告
	runner = unittest.TextTestRunner()

	runner.run(suite)

user01 = TestLogin()