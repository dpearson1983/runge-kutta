import numpy as np
import rungekutta
import matplotlib.pyplot as plt

k = float(input("Enter value of the spring constant: "))
m = float(input("Enter value of the mass: "))

def f(t, y):
    if (len(y) != 2):
        print("Improper y array size in function f(t,y). Must be 2 elements only.")
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -(k/m)*y[0]
    return F

h = float(input("Enter the desired time step: "))
N = int(input("Enter the number of time steps: "))
t = np.zeros(N)
x = np.zeros(N)
v = np.zeros(N)

y = np.zeros(2)
y[0] = float(input("Enter the starting position: "))

for i in range(0, N):
    t[i] = i*h + h
    y = rungekutta.rk2(t[i], y, h, f)
    x[i] = y[0]
    v[i] = y[1]
    
f = open("rk2Spring.dat", "w")
for i in range(0, N):
    f.write(str(t[i]) + " " + str(x[i]) + " " + str(v[i]) + "\n")
f.close()
    
plt.plot(t, x, 'o')

plt.show()
