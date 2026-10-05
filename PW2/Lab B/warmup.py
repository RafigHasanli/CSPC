"""
PW2 Lab B Part 2 -- three routes to a minimum.
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

def grad_descent(dfun,x0,lr=0.01,tol=1e-10,maxit=100000):
    x=x0
    for i in range(maxit):
        step=lr*dfun(x)
        x=x-step
        if abs(step)<tol:
            break
    return x

print("--- 2A: f(x)=(x-3)^2+1, x0=0 ---")
print("gradient descent:",grad_descent(df,0))
print("newton:          ",newton(df,0,fprime=d2f))
print("SLSQP:           ",minimize(f,0,method="SLSQP").x[0])

# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

for x0 in [0,2]:
    print("\n--- 2B: g(x), x0=%s ---"%x0)

    xg=grad_descent(dg,x0)
    print("gradient descent:",xg,"g=",g(xg))

    xn=newton(dg,x0,fprime=d2g)
    kind="minimum" if d2g(xn)>0 else "maximum"
    print("newton:          ",xn,"g''=",d2g(xn),"->",kind)

    xs=minimize(g,x0,method="SLSQP").x[0]
    print("SLSQP:           ",xs,"g=",g(xs))