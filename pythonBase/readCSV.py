import csv

with open('../testFile/userInfo.csv', newline='') as f:
	reader = csv.reader(f)
	for row in f:
		print(row)
