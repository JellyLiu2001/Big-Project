import xlrd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np



workbook = xlrd.open_workbook('T_data数据汇总.xlsx')
xl_sheet = workbook.sheet_by_index(0)
# reading all the data from the excel file and naming them with the relative name
T_date = xl_sheet.row_values(1)#总日期
T_income = xl_sheet.row_values(2)#总收入
T_psrate = xl_sheet.row_values(3)#总客座率
T_outcome = xl_sheet.row_values(4)#总支出
T_flight = xl_sheet.row_values(5)#总航班数
T_sick = xl_sheet.row_values(6)#总生病人数

# making it easy for later calculation by using numpy
x=T_date[1:]
psrate=np.array(T_psrate[1:])
flight=np.array(T_flight[1:])
income=np.array(T_income[1:])
outcome=np.array(T_outcome[1:])
sick=np.array(T_sick[1:])


# in order to put all the plots into one graph, dividing all the values in all 5 list with a different constant to make them suitable to be put together
y1 = psrate
y2 = flight/100
y3 = income/10
y4 = outcome/10
y5 = sick/1000

# plotting the graph and labelling all the lines with the units
plt.plot(x,y1, label = "passenger rate(percents)")
plt.plot(x,y2, label = "numbers of flight(hundreds)")
plt.plot(x,y3, label = "amount of income(billions)")
plt.plot(x,y4, label = "amount of outcome(billions)")
plt.plot(x,y5, label = "number of cases(thousands)")
plt.xlabel('date')
plt.legend()
plt.show()