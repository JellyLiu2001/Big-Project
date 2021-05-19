import xlrd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt




workbook = xlrd.open_workbook('T_data数据汇总.xlsx')
xl_sheet = workbook.sheet_by_index(0)
# reading all the data from the excel file and naming them with the relative name
T_date = xl_sheet.row_values(1)[1:]#总日期
T_income = xl_sheet.row_values(2)[1:] #总收入
T_psrate = xl_sheet.row_values(3)[1:]#总客座率
T_outcome = xl_sheet.row_values(4)[1:]#总支出
T_flight = xl_sheet.row_values(5)[1:]#总航班数
T_sick = xl_sheet.row_values(6)[1:]#总生病人数



# making it easy for later calculation by using numpy
x=T_date
incomes=T_income
psrate=np.array(T_psrate)
flight=np.array(T_flight)
income=np.array(T_income)
outcome=np.array(T_outcome)


# in order to put all the plots into one graph, dividing all the values in all 5 list with a different constant to make them suitable to be put together
y1 = psrate
y2 = flight/100
y3 = income/10
y4 = outcome/10


# plotting the graph and labelling all the lines with the units

plt.plot(x, y1, label = "Passenger Rate(%)")
plt.plot(x, y2, label = "Number of Flights(Hundreds)")
plt.plot(x, y3, label = "Amount of Income(billion RMB)")
plt.plot(x, y4, label = "Amount of Outcome(billion RMB)")
plt.legend()
plt.xlabel("Months")
plt.show()

