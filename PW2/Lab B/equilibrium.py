"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

def k_imbalance(x):
    return (2*x)**2/((a-x)*(b-x))-K

# method 1: root-finding
x_newton=newton(k_imbalance,0.5)

# method 2: minimise the squared imbalance
res=minimize(lambda x:k_imbalance(x[0])**2,x0=[0.5],method="SLSQP",bounds=[(0,0.999)])
x_slsqp=res.x[0]

print("newton:",x_newton)
print("SLSQP: ",x_slsqp)
print("H2 =",a-x_newton,"mol")
print("I2 =",b-x_newton,"mol")
print("HI =",2*x_newton,"mol")

xs=np.linspace(0,0.999,200)
plt.plot(xs,a-xs,label="H2")
plt.plot(xs,b-xs,"--",label="I2")
plt.plot(xs,2*xs,label="HI")
plt.axvline(x_newton,color="k",linestyle=":",label="equilibrium")
plt.xlabel("extent x (mol)")
plt.ylabel("amount (mol)")
plt.legend()
plt.savefig("equilibrium.png")