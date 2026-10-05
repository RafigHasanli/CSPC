"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""

import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("titration.csv",delimiter=",",skiprows=1)
V=data[:,0]
pH=data[:,1]

slope=np.gradient(pH,V)
i=np.argmax(slope)
print("equivalence point: %.1f mL"%V[i])

fig,ax=plt.subplots(1,2,figsize=(10,4))

ax[0].plot(V,pH)
ax[0].axvline(V[i],color="r",linestyle="--")
ax[0].set_xlabel("volume of base (mL)")
ax[0].set_ylabel("pH")
ax[0].set_title("titration curve")

ax[1].plot(V,slope)
ax[1].axvline(V[i],color="r",linestyle="--")
ax[1].set_xlabel("volume of base (mL)")
ax[1].set_ylabel("dpH/dV")
ax[1].set_title("slope")

plt.tight_layout()
plt.savefig("titration.png")