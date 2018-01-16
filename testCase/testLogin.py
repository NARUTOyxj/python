import csv
# date = csv.reader(open('../testFile/userInfo.csv','r'))

class testLogin(ConfigHttp):
	"""docstring for testCase"""

	def __init__(self, fileName):
		self.fileName = fileName

	def getData(self):
		path = '../testFile/' + self.fileName
		with open(path, newline='') as f:
			reader = csv.reader(f)
			for i,rows in enumerate(f):
				if i == 1:
					print(rows)

login = testLogin('userInfo.csv')
login.geturl()
login.getData()




