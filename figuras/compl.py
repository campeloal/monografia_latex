import matplotlib.pyplot as plt
import numpy as np


xVertAxis = [1,2,3,4,5,6,7,8,9,10]
constant = [20,20,20,20,20,20,20,20,20,20]
n = [1,2,3,4,5,6,7,8,9,10]
quad = [1,4,9,16,25,36,49,64,81,100]
cubic = [1,8,27,64,125,216,343,512,729,1000]
log = [np.log(1),np.log(2),np.log(3),np.log(4),np.log(5),np.log(6),
       np.log(7),np.log(8),np.log(9),np.log(10)]
nlog = [np.log(1),2 * np.log(2),3 * np.log(3),4 * np.log(4),5 * np.log(5),6 * np.log(6),
       7 * np.log(7), 8 * np.log(8), 9 * np.log(9),10 * np.log(10)]

exp = [np.exp(1),np.exp(2),np.exp(3),np.exp(4),np.exp(5),np.exp(6),
       np.exp(7),np.exp(8),np.exp(9),np.exp(10)]

plt.title('Algorithm Complexity')
plt.xlabel('Number of Inputs')
plt.ylabel('Resulting size')
plt.plot(xVertAxis, constant, 'y-',label='Constant')
plt.plot(xVertAxis, n, 'b-', label = "Linear")
plt.plot(xVertAxis, quad, 'r-', label = "Quadric")
plt.plot(xVertAxis, cubic, 'g-', label = "Cubic")
plt.plot(xVertAxis, log, 'm-', label = "Log N")
plt.plot(xVertAxis, nlog, 'c-', label = "N Log N")
plt.plot(xVertAxis, nlog, 'k-', label = "Exponential")
plt.legend(loc="upper left", bbox_to_anchor=[0.7, 1.0],
           ncol=1, shadow=True, title="Legend")

plt.show()
