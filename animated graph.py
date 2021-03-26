import ffmpeg
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

covid = pd.read_excel('new data for graph.xlsx',skiprows =1)
def get_data(table,rownum,title):
    data = pd.DataFrame(table.loc[rownum][2:]).astype(float)
    data.columns = {title}
    return data

title = ''
incomes = get_data(covid,0,title)
psrates = get_data(covid,1,title)
outcomes = get_data(covid,2,title)
flights = get_data(covid,3,title)
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

x1 = np.array(incomes.index)
y1 = np.array(incomes[''])
x2 = np.array(outcomes.index)
y2 = np.array(outcomes[''])
x3 = np.array(psrates.index)
y3 = np.array(psrates[''])
x4 = np.array(flights.index)
y4 = np.array(flights[''])
x5 = np.array(sicks.index)
y5 = np.array(sicks[''])

X1,Y1 = augment(x1,y1,10)
X2,Y2 = augment(x2,y2,10)
X3,Y3 = augment(x3,y3,10)
X4,Y4 = augment(x4,y4,10)
X5,Y5 = augment(x5,y5,10)


income = pd.DataFrame(Y1,X1)
income.columns = {title}
outcome = pd.DataFrame(Y2,X2)
outcome.columns = {title}
psrate = pd.DataFrame(Y3,X3)
psrate.columns = {title}
flight = pd.DataFrame(Y4,X4)
flight.columns = {title}
sick = pd.DataFrame(Y5,X5)
sick.columns = {title}

Writer = animation.writers['ffmpeg']
writer = Writer(fps=100, metadata=dict(artist='Me'), bitrate=2600)

fig = plt.figure(figsize=(10,6))
plt.xlim(1, 8.3)
plt.ylim(0, 160)
plt.xlabel('months',fontsize=20)
plt.ylabel(title,fontsize=20)
plt.title('covid per months',fontsize=20)

def animate(i):
    d1 = income.iloc[:int(i+1)]#select data range
    d2 = outcome.iloc[:int(i+1)]
    d3 = psrate.iloc[:int(i+1)]
    d4 = flight.iloc[:int(i+1)]
    d5 = sick.iloc[:int(i+1)]
    p = sns.lineplot(x=d1.index, y=d1[title], data=d1, color="r")
    p = sns.lineplot(x=d2.index, y=d2[title], data=d2, color="g")
    p = sns.lineplot(x=d3.index, y=d3[title], data=d3, color="b")
    p = sns.lineplot(x=d4.index, y=d4[title], data=d4, color="y")
    p = sns.lineplot(x=d5.index, y=d5[title], data=d5, color="c")
    p.tick_params(labelsize=10)
    plt.setp(p.lines,linewidth=2)


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=250, repeat=False)
plt.show()