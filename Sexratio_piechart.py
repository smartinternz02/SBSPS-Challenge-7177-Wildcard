from matplotlib import pyplot as plt
import numpy as np
  
  
# Creating dataset
districts = ['HYDERABAD', 'MEDAK', 'WARANGAL(U)', 'SANGAREDDY', 'RANGAREDDY']  
data = [954,1027,997,965,950]
cols = ['c','m','r','g','b']

plt.pie(data, labels=districts,colors=cols,startangle=90,explode=(0,0,0,0,0),autopct='%1.1f%%')

plt.title('Sex Ratio')
plt.show()
