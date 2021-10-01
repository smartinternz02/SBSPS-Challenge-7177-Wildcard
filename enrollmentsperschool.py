
import matplotlib.pyplot as plt
import numpy as np
  
# create data
x = np.arange(5)
y1 = [202.0338658,59.28062016,67.55614973,70.44456641,73.32340862]
y2 = [208.7024648,128.3492063,100.6448087,121.8951613,149.5419355]

width = 0.2
  
# plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width, color='cyan')
plt.bar(x, y2, width, color='orange')
#plt.bar(x+0.2, y3, width, color='green')
plt.xticks(x, ['HYDERABAD', 'MEDAK', 'WARANGAL(U)', 'SANGAREDDY', 'RANGAREDDY'])
plt.xlabel("DISTRICTS")
plt.ylabel("ENROLLMENT PER SCHOOL")
plt.legend(["Primary Enrollment Per School", "Upper Primary Enrollment Per School"])
plt.title('ENROLLMENTS')
plt.show()