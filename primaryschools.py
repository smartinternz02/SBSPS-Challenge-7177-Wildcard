import matplotlib.pyplot as plt
import csv
import pandas as pd
plt.style.use('bmh')
df=pd.read_csv('lit_rate.csv')
x=df['Districts'].head(5)
y=df['Primary Schools'].head(5)

plt.title('NUMBER OF PRIMARY SCHOOLS IN FIVE DISTRICTS')

plt.xlabel('Districts',fontsize=10)
plt.ylabel('Number of primary schools',fontsize=10)
plt.bar(x,y)
plt.show()