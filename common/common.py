import os
from xlrd import open_workbook
import sys
sys.path.append('..\\testFile')
import readConfig

# 从excel文件中读取测试用例
def get_xls(xls_name, sheet_name):
    cls = []
    # get xls file's path
    xlsPath = os.path.join('..\\testFile', xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
            print(cls)

def common_args(sys):
    readData = readConfig.ReadConfig()
    token = readData.get_section('token','token') 
    data = {'token': token,'apiVer':'','sign':'','fromSys':sys,'lang':'zh'}
    return data

# get_xls("userInfo.xlsx", "Sheet1")
# common_args('ship')
