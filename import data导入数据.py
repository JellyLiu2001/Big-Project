import xlrd#导入Excel库
T_sheet = xlrd.open_workbook("T_data数据汇总.xlsx")#设置表格路径
xl_sheet = T_sheet.sheet_by_index(0)#设置表格中的sheet
T_date = xl_sheet.row_values(1)#总日期
T_income = xl_sheet.row_values(2)#总收入
T_psrate = xl_sheet.row_values(3)#总客座率
T_outcome = xl_sheet.row_values(4)#总支出
T_flight = xl_sheet.row_values(5)#总航班数
T_sick = xl_sheet.row_values(6)#总生病人数
T_new = xl_sheet.row_values(7)#新增感染人数
f = open('data.txt',mode='w')   
f.write('hello there is the data \n')  # write 写入
A_mode= [T_date,T_income,T_outcome,T_flight,T_sick,T_new]
A_data=[]
for i in range(len(A_mode)):
    A_data.append=str(A_mode[i])
    
f.writelines(A_data)
f.close()#关闭文件