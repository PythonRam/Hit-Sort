import matplotlib.pyplot as plt
import numpy as np
row1=np.array([5000,10000,15000,20000,25000,30000])
##### For 5000 values in an array it took 0.1412... seconds 
##### And I know you can figure it out
row2=np.array([0.141219139099,0.515411138535,1.12829589844,2.05562114716,3.1011929512,4.53416204453])
plt.plot(row1,row2, 'k')
plt.axis([0,30000,0,5])
plt.show()


