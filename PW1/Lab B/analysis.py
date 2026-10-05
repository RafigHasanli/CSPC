import numpy as np 

data=np.loadtxt("freefall.csv", delimiter="," , skiprows=1)

t=data[:,0]
y=data[:,1]

v=np.gradient(y,t)
a=np.gradient(v,t)

print("mean acceleration:",a.mean())