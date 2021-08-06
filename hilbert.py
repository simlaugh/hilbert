import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert2, chirp
import csv
rf_matrix = np.loadtxt(open("RF.csv","rb"),delimiter=',',skiprows=0)
analytic_signal = hilbert2(rf_matrix,None)
analytic_signal

hilbert_data = np.abs(analytic_signal)
np.savetxt('Hilbert.csv',hilbert_data,delimiter=',')
hilbert_data
