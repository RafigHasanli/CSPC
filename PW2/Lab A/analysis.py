#Checkpoint 3
import numpy as np 

data=np.loadtxt("freefall.csv", delimiter="," , skiprows=1)

t=data[:,0]
y=data[:,1]

v=np.gradient(y,t)
a=np.gradient(v,t)

print("mean acceleration:",a.mean())
print("std:",a.std())

#Checkpoint 4

from scipy.integrate import cumulative_trapezoid

v2=cumulative_trapezoid(a,t,initial=0)+v[0]
y2=cumulative_trapezoid(v2,t,initial=0)+y[0]

print("max difference:",np.abs(y2-y).max())

#Checkpoint 5

import matplotlib.pyplot as plt

fig,ax=plt.subplots(3,1,sharex=True,figsize=(8,9))

ax[0].plot(t,y)
ax[0].set_ylabel("position (m)")

ax[1].plot(t,v)
ax[1].set_ylabel("velocity (m/s)")

ax[2].plot(t,a)
ax[2].axhline(-9.81,color="r",linestyle="--",label="-9.81")
ax[2].set_ylabel("acceleration (m/s²)")
ax[2].set_xlabel("time (s)")
ax[2].legend()

plt.tight_layout()
plt.savefig("motion.png")