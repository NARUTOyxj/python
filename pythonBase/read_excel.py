import openpyxl

class testCase(object):
	"""docstring for testCase"""

	def __init__(self, path):
		self.path = path

	def read07Excel(self):
    wb = openpyxl.load_workbook(self.path)
    sheet = wb.get_sheet_by_name('userInfo1.xlsx')

    for row in sheet.rows:
        for cell in row:
            print(cell.value, "\t", end="")
        print()

test = testCase('../testFile/')
test.getData()
