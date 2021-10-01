import matplotlib.pyplot as plt
import csv
import pandas as pd
plt.style.use('bmh')
df=pd.read_csv('lit_rate.csv')
x=df['Districts'].head(5)
y=df['Households'].head(5)
plt.title('Households in 5 Districts of Telangana')
plt.xlabel('Districts',fontsize=10)
plt.ylabel('Households',fontsize=10)
plt.bar(x,y)
plt.show()