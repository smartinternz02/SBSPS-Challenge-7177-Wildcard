import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = np.arange(5)
y1 = [0,708574,340351,997663,1026113]

y2 = [3943323,58854,740507,529965,1420152] 

width = 0.2
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width, color='cyan')
plt.bar(x, y2, width, color='orange')
#plt.bar(x+0.2, y3, width, color='green')
plt.xticks(x, ['HYDERABAD', 'MEDAK', 'WARANGAL(U)', 'SANGAREDDY', 'RANGAREDDY'])
plt.xlabel("DISTRICTS")
plt.ylabel("POPULATION")
plt.legend(["Rural Population", "Urban Population"])
plt.title('Rural-Urban')
plt.show()