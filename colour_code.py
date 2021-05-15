
import xlrd#导入Excel库
T_sheet = xlrd.open_workbook("T_data数据汇总.xls")#设置表格路径
xl_sheet = T_sheet.sheet_by_index(0)#设置表格中的sheet
T_date = xl_sheet.row_values(1)#总日期
T_income = xl_sheet.row_values(2)#总收入
T_psrate = xl_sheet.row_values(3)#总客座率
T_outcome = xl_sheet.row_values(4)#总支出
T_flight = xl_sheet.row_values(5)#总航班数
T_sick = xl_sheet.row_values(6)#总生病人数
T_new = xl_sheet.row_values(7)#新增感染人数
# print(T_date,T_income,T_psrate,T_outcome,T_flight,T_sick,T_new)#打印所有数据


# insert 'plane' image for map animation 
from PIL import Image
myImage = Image.open("images\plane.jpg");
# myImage.show()

# identify the cases of the day by three classes (test)
int_new = 1
# print(T_new[int_new])
if T_new[int_new] == 0:
    print("无")
    # colour = green
elif 0 < T_new[int_new] <=5:
    print("有")
    # colour = orange
else:
    print("多")
    # colour = red
int_new = int_new + 1    

# print(T_new[int_new])
if T_new[int_new] == 0:
    print("无")
elif 0 < T_new[int_new] <=5:
    print("有")
else:
    print("多")
int_new = int_new + 1    

# print(T_new[int_new])
# print(int_new)
if T_new[int_new] == 0:
    print("无")
elif 0 < T_new[int_new] <=5:
    print("有")
else:
    print("多")


# change colour of 'plane' depends on cases on the day






































































