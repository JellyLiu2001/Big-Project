import xlrd
T_sheet = xlrd.open_workbook("T_data数据汇总.xls")
xl_sheet = T_sheet.sheet_by_index(0)
print ('Sheet name: %s' % xl_sheet.name)
cols = xl_sheet.col_values(2)
print(cols)