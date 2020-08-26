import numpy as np

def rk2(t, y, h, f, k, m):
    k_1 = h*f(t, y, k, m)
    k_2 = h*f(t+h/2.0,y+k_1/2.0, k, m)
    y = y + k_2
    return y
    
