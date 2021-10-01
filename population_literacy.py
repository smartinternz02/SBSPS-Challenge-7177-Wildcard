import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = np.arange(5)
y1 = [2892155, 377984, 746460, 853960, 1543959]
y2 = [2412787, 220539, 575237, 558250, 1121900 ]

width = 0.2
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width, color='cyan')
plt.bar(x, y2, width, color='orange')
#plt.bar(x+0.2, y3, width, color='green')
plt.xticks(x, ['HYDERABAD', 'MEDAK', 'WARANGAL(U)', 'SANGAREDDY', 'RANGAREDDY'])
plt.xlabel("DISTRICTS")
plt.ylabel("POPULATION")
plt.legend(["Population", "Literate population"])
plt.title('LITERACY')
plt.show()