# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 13:35:03 2015

@author: chris
"""

import numpy as np
from scipy import signal
from scipy.optimize import root
import matplotlib.pylab as plt

run_1 = np.genfromtxt('/home/chris/Documents/Phys 120b/YBCO Superconductor/Run 1.txt')
data = np.genfromtxt('/home/chris/Documents/Phys 120b/YBCO Superconductor/Data.txt')

T_1 = run_1[:,0]*-1
V_1 = run_1[:,1]

Temperature = data[:,0]
V = data[:,1]*-1

y = signal.savgol_filter(V, 5, 2, deriv=2, mode='nearest')
#y_1 = signal.savgol_filter(V_1, 5, 4, deriv=2)


plt.figure(num=1)
plt.plot(T_1, V_1, 'b.')

plt.figure(num=2)
plt.plot(Temperature, V, 'b.', Temperature, y, 'r--')
plt.grid()
plt.show()