import csv

date = csv.reader(open('../testFile/userInfo.csv','r'))

for user in date:
	print(user)
	print(date[0])



