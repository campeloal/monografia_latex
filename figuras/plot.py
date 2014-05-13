import matplotlib.pyplot as plt
import numpy as np


xVertAxis = [1000,2500,5000,7500,10000,15000,20000,25000,30000]
yVertAxis = [288740,312955,385954,513838,664805,940012,1206179,1924849,3172130]
plt.subplot(211)
plt.title('Phong Shader')
plt.xlabel('Number of Polygons')
plt.ylabel('Render time (ns)')
plt.plot(xVertAxis, yVertAxis, 'b-')
plt.plot(xVertAxis, yVertAxis, 'ro')
plt.show()


xVertAxis = [1000,2500,5000,7500,10000,15000,20000,25000,30000]
yVertAxis = [np.log(288740),np.log(312955),np.log(385954),np.log(513838),np.log(664805),np.log(940012),np.log(1206179),np.log(1924849),np.log(3172130)]
plt.subplot(211)
plt.title('Phong Shader')
plt.xlabel('Number of Polygons')
plt.ylabel('Render time (ns)')
plt.plot(xVertAxis, yVertAxis, 'b-')
plt.plot(xVertAxis, yVertAxis, 'ro')
plt.show()
