import matplotlib.pyplot as plt
import csv
import datetime

x = []
y = []

with open('index.csv','rU') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        y.append(float(row[0]))
        x.append((row[1]))

plt.plot(x,y, label='Dolar/TL Kur')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()