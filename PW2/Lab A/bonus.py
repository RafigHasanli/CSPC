import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("trajectory.csv",delimiter=",",skiprows=1)
t=data[:,0]
x=data[:,1]
y=data[:,2]

vx=np.gradient(x,t)
vy=np.gradient(y,t)
speed=np.sqrt(vx**2+vy**2)

fig,ax=plt.subplots(1,2,figsize=(10,4))

ax[0].plot(x,y)
ax[0].set_xlabel("x (m)")
ax[0].set_ylabel("y (m)")
ax[0].set_title("path")

ax[1].plot(t,speed)
ax[1].set_xlabel("time (s)")
ax[1].set_ylabel("speed (m/s)")
ax[1].set_title("speed")

plt.tight_layout()
plt.savefig("trajectory.png")