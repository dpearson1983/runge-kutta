import numpy as np
import rungekutta
import matplotlib.pyplot as plt
import sys

k = 0.0
m = 0.0
x_0 = 0.0
h = 0.0
N = 0
err_tol = 0.0

for i in range(0,len(sys.argv)):
    if (sys.argv[i] == "-k"):
        k = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-m"):
        m = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-x_0"):
        x_0 = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-h"):
        h = float(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-N"):
        N = int(sys.argv[i+1])
        i += 1
    elif (sys.argv[i] == "-err_tol"):
        err_tol = float(sys.argv[i+1])
        i += 1

def f(t, y):
    if (len(y) != 2):
        print("Improper y array size in function f(t,y). Must be 2 elements only.")
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -(k/m)*y[0]
    return F

t_max = N*h
t_now = 0.0
t = np.empty(0)
x = np.empty(0)
v = np.empty(0)
h_min = h/64.0
h_max = h*64.0

y = np.zeros(2)
y[0] = x_0
i = 0
while (t_now < t_max):
    t = np.append(t, i*h + h)
    t_now = i*h + h
    h, y = rungekutta.rk45(t[i], y, h, f, err_tol, h_min, h_max)
    x = np.append(x, y[0])
    v = np.append(v, y[1])
    i += 1
    
f = open("rk45Spring.dat", "w")
for i in range(0, len(t)):
    f.write(str(t[i]) + " " + str(x[i]) + " " + str(v[i]) + "\n")
f.close()
    
plt.plot(t, x, 'o')

plt.show()
