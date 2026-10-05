import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

data=np.loadtxt("kinetics.csv",delimiter=",",skiprows=1)
t=data[:,0]
C=data[:,1]
C0=C[0]

def total_error(k):
    return np.sum((C-C0*np.exp(-k[0]*t))**2)

res=minimize(total_error,x0=0.5,method="SLSQP",bounds=[(0,5)])
k=res.x[0]
print("fitted k:",k)

plt.scatter(t,C,label="data")
plt.plot(t,C0*np.exp(-k*t),color="r",label="fit, k=%.3f"%k)
plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.savefig("kinetics.png")