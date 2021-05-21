import ffmpeg
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

covid = pd.read_excel('T_data 数据汇总.xlsx',skiprows =1)
def get_data(table,rownum,title):
    data = pd.DataFrame(table.loc[rownum][2:]).astype(float)
    data.columns = {title}
    return data

title = ''
sicks = get_data(covid,4,title)

def augment(xold,yold,numsteps):
    xnew = []
    ynew = []
    for i in range(len(xold)-1):
        difX = xold[i+1]-xold[i]
        stepsX = difX/numsteps
        difY = yold[i+1]-yold[i]
        stepsY = difY/numsteps
        for s in range(numsteps):
            xnew = np.append(xnew,xold[i]+s*stepsX)
            ynew = np.append(ynew,yold[i]+s*stepsY)
    return xnew,ynew


def predictedcases(startnum):
    n=0    
    predicted = [startnum, startnum+ random.randint(0,30)]
    while True:
        if len(predicted) < 23:
            newcases = random.randint(0,50)
            nextmonth = predicted[n+1] + newcases
            predicted.append(nextmonth)    
            n+= 1
        else:
            break
    return predicted

x3 = np.array(range(1,24))
y3 = np.array(predictedcases(82725))
x5 = np.array(sicks.index)
y5 = np.array(sicks[''])

X3,Y3 = augment(x3,y3,10)
X5,Y5 = augment(x5,y5,10)

predictedsick = pd.DataFrame(Y3,X3)
predictedsick.columns = {title}
sick = pd.DataFrame(Y5,X5)
sick.columns = {title}


Writer = animation.writers['ffmpeg']
writer = Writer(fps=100, metadata=dict(artist='Me'), bitrate=2600)


fig = plt.figure(figsize=(10,6))
plt.xlim(1, 8.3)
plt.ylim(82600 , 83500)
plt.xlabel('Months',fontsize=10)
plt.ylabel('Total Cases',fontsize=10)
plt.title('Covid cases per months',fontsize=20)

def animate(i):

    d1 = sick.iloc[:int(i+1)]#select data range
    d2 = predictedsick.iloc[:int(i+1)]
    
    p = sns.lineplot(x=d1.index, y=d1[title], data=d1, color="r")
    p = sns.lineplot(x=d1.index, y=d2[title], data=d2, color="b")

    p.tick_params(labelsize=10)
    plt.setp(p.lines,linewidth=2)
    plt.legend(['real number of cases','predicted number of cases'])



ani = matplotlib.animation.FuncAnimation(fig, animate, frames=240, repeat=False)
plt.show()

