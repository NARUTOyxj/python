import csv

class testCase(object):
	"""docstring for testCase"""

	def __init__(self, fileName):
		self.fileName = fileName

	def getData(self):
		path = '../testFile/' + self.fileName
		with open(path, newline='') as f:
			reader = csv.reader(f)
			for row in f:
				print(row)

test = testCase('userInfo.csv')
test.getData()


		
