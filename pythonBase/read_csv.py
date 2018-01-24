import csv

class testCase(object):
	"""docstring for testCase"""

	def __init__(self, fileName):
		self.fileName = fileName

	def getData(self):
		path = 'D:/SCM/python/testFile/' + self.fileName
		with open(path, newline='') as f:
			reader = csv.reader(f)
			for i,rows in enumerate(f):
				if i > 0:
					print(rows)

test = testCase('userInfo.csv')
test.getData()


		
