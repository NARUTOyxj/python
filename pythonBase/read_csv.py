import csv
import io

class testCase(object):
	"""docstring for testCase"""

	def __init__(self, fileName):
		self.fileName = fileName

	def getData(self):
		path = '../testFile/' + self.fileName
		with open(path, newline='') as f:
			reader = csv.DictReader(f)
			for row in reader:
				print(row['nickname'],row['password'])
			

test = testCase('userInfo.csv')
test.getData()


		
