import numpy as np
import math
import rungekutta

def f(t,y,k,m):
    if (len(y) != 2):
        print("In proper y array size for function f(t,y,k,m). Must be 2 elements only")
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -(k/m)*y[0]
    return F

h = float(input("Enter the desired time step: "))
N = int(input("Enter the number of time steps: "))
t = np.zeros(N)
y = np.zeros(2)
y[0] = float(input("Enter the starting position (i.e. amplitude of oscillations): "))
k = float(input("Enter the spring constant: "))
m = float(input("Enter the mass: "))

x = np.zeros(N)
v = np.zeros(N)

for i in range(0,N):
    t[i] = i*h
    y = rungekutta.rk2(t[i], y, h, f, k, m)
    x[i] = y[0]
    v[i] = y[1]
    
f = open("rk2Spring.dat", "w")
for i in range(0,N):
    f.write(str(t[i]) + " " +  str(x[i]) + " " + str(v[i]) + "\n")
    
f.close()
        
