
# f(x0, x1) = x0^2+x1^2 (x0=3, x1=4)

import numpy as np

def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h)-f(x-h))/(2*h)

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2 + x1*x1

print(numerical_diff(function_tmp1, 3))
print(numerical_diff(function_tmp2, 4))
