import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = np.arange(5)
y1 = [86.99, 67.51, 84.4, 73.02, 78.94]
y2 = [79.35, 45.98,67.98, 54.84, 64.63 ]

width = 0.2
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width, color='cyan')
plt.bar(x, y2, width, color='orange')
#plt.bar(x+0.2, y3, width, color='green')
plt.xticks(x, ['HYDERABAD', 'MEDAK', 'WARANGAL(U)', 'SANGAREDDY', 'RANGAREDDY'])
plt.xlabel("DISTRICTS")
plt.ylabel("LITERACY RATES")
plt.legend(["Male literacy rate", "female literacy rate"])
plt.title('LITERACY RATE')
plt.show()