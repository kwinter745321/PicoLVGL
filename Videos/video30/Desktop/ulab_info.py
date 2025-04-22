# ulab_info.py
#
# Print information about the specific build of ulab 
#
# This program is from ulab 6.7.3 online documentation
# obtained 19 Apil 2025
# https://micropython-ulab.readthedocs.io/en/latest/ulab-intro.html#customising-the-firmware
# MIT License
#
import ulab
from ulab import numpy as np
from ulab import scipy as spy

import sys
print("PyLang", sys.version_info, ";", sys.implementation)

version = ulab.__version__
version_dims = version.split('-')[1]
version_num = int(version_dims.replace('D', ''))

print('version string: ', version)
print('version dimensions: ', version_dims)
print('numerical value of dimensions: ', version_num)

if len(np.fft.fft(np.zeros(4))) == 2:
    print('FFT is NOT numpy compatible (real and imaginary parts are treated separately)')
else:
    print('FFT is numpy compatible (complex inputs/outputs)')
    

print('===== constants, functions, and modules of numpy =====\n\n', dir(np))

# since fft and linalg are sub-modules, print them separately
print('\nfunctions included in the fft module:\n', dir(np.fft))
print('\nfunctions included in the linalg module:\n', dir(np.linalg))

print('\n\n===== modules of scipy =====\n\n', dir(spy))
print('\nfunctions included in the optimize module:\n', dir(spy.optimize))
print('\nfunctions included in the signal module:\n', dir(spy.signal))
print('\nfunctions included in the special module:\n', dir(spy.special))

#Methods
print("#### Methods included ############################")
print(dir(np.array))


print("#### Operators included ############################")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

try:
    print(a ** b)
except Exception as e:
    print('operator is not supported: ', e)
    
 


