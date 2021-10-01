from matplotlib import pyplot as plt
import numpy as np
  
  
# Creating dataset
districts = ['HYDERABAD', 'MEDAK', 'WARANGAL(U)', 'SANGAREDDY', 'RANGAREDDY']
  
data = [83.43,58.35,77.06,65.37,72.66]
  
# Creating plot
cols = ['c','m','r','g','b']

plt.pie(data, labels=districts,colors=cols,startangle=90,explode=(0,0,0,0,0),autopct='%1.1f%%')

plt.title('Literacy Rate')
plt.show()
