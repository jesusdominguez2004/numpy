# W3Schools, NumPy Ufunc Finding LCM
import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)
