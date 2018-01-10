import openpyxl

def read07Excel(path):
	wb = openpyxl.load_workbook(path)
	sheet = wb.get_sheet_by_name('userInfo1.xlsx')

	for row in sheet.rows:
		for cell in row:
			print(cell.value, "\t", end="")
			print()

read07Excel(r'../testFile/')