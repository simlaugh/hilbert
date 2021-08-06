import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert2
import csv

rf_matrix = np.loadtxt(open("RF.csv","rb"),delimiter=',',skiprows=0)
analytic_signal = hilbert2(rf_matrix,None)

print(analytic_signal)

hilbert_data = np.abs(analytic_signal)
np.savetxt('Hilbert.csv',hilbert_data,delimiter=',')
print(hilbert_data)
plt.imshow(hilbert_data,cmap='hot',aspect='auto')  
plt.show()
