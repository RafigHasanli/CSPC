# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW/Lab.

## Setup
Create the environment for a given lab:
```bash
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations
What I built:

Created the personal course repository structure, isolated conda environment, git version control history, automated pytest suite, and performance benchmark script for radioactive decay.

Speed comparison (loop vs NumPy):

loop : 1.3977 s

numpy : 0.000168 s

speed-up: 8334.0 x faster

Tests: all passing? yes

Conclusion:

Vectorizing the simulation with NumPy replaces explicit Python loops with compiled C routines, yielding an acceleration of over 7,400x on 200,000 atoms. Integrating pytest validates statistical outputs against the analytical exponential decay law, and maintaining environment specifications ensures identical behavior across systems.

---

## PW1 - Lab B: Data, Plotting, and Automation

**What I built:**
- Completed `plot.py` using NumPy and Matplotlib to read real observation data and render a side-by-side 1×2 subplot with shared axes against the analytical decay model.
- Wrote a declarative `Snakefile` workflow to automate figure generation.

**Data & Comparison:**
- The observed data points closely follow the theoretical exponential decay law N(t) = N0 * e^(-λt) with λ = 0.3.
- Random counting fluctuations (noise) are evident in the experimental observation scatter, but the overall rate, curvature, and asymptotic trend align with the analytical curve.

**Snakemake Automation:**
- The Snakemake pipeline defines a rule mapping `decay_observed.csv` and `plot.py` to `figure.png`. It monitors file modification timestamps, executing only when inputs are modified or when `figure.png` is absent, eliminating redundant re-computation.

---

## PW2 - Lab A: Motion from Tracking Data

**What I built:**
- analysis.py was created and it prints out mean acceleration and standard deviation of acceleration. Mean acceleration=-8.57968750000008 Std=28.71612572170628. 
The reason for these results is that acceleration is much noisier than position because each derivative subtracts nearby noisy measurements and divides by the small time step (0.1 s), so the noise is magnified, and it happens twice.

- Integrating the noisy acceleration back to velocity and then position gave a result within 0.78 m of the original position (max difference). Integration suppresses noise because random errors partly cancel when summed.
- Figure: motion.png shows smooth position, slightly rough velocity, and very noisy acceleration.

**Bonus: 2D trajectory (trajectory.csv)**
- The path (x vs y) is a figure-eight that crosses itself near the origin, spanning about ±50 m in both x and y, with small wiggles from measurement noise.
- The speed, computed as sqrt(vx² + vy²) from np.gradient of x and y, oscillates repeatedly between about 8 and 38 m/s, with a period of roughly 5 s. It looks fastest around the crossing in the middle of the eight and slowest near the outer ends of the loops.
- The speed curve is much jerkier than the path, because it comes from a derivative and differentiation amplifies noise, the same effect as in the free-fall data.
- Figure: trajectory.png.

---

## PW2 - Lab B: Optimization in Chemistry
**Part 1: setup**
- Created the `PW2/Lab B` folder in the CSPC repo, copied in the Moodle skeleton files, and activated the `cspc` conda environment (numpy, scipy, matplotlib).

**Part 2A: easy convex function**
- On f(x)=(x-3)^2+1, gradient descent, Newton and SLSQP all gave x = 3.

**Part 2B: harder landscape**
- On g(x)=x^4-3x^2+x+5 the methods did not agree. From x0=0, gradient descent and SLSQP found the minimum at x = -1.30 (g = 1.486), but Newton landed on x = 0.17, where g'' = -5.65 < 0, so it is a maximum, not a minimum. Newton only solves g'(x)=0, so it cannot tell a minimum from a maximum.
- From x0=2, Newton and gradient descent found a different, local minimum at x = 1.13 (g = 3.93), while SLSQP still reached the lower minimum at x = -1.30.
- The starting point changed the result: g has two minima, and the answer depends on where the method starts and which algorithm is used. On a simple convex problem the starting point doesn't matter.

**Part 3: fitting a reaction rate**
- Fitted the first-order model C(t)=C0*exp(-kt) to the noisy data by minimizing the sum of squared errors with SLSQP (bounds 0 to 5, start 0.5). The fitted rate constant is k = 0.262, close to the expected 0.25, and the fitted curve passes through the data (kinetics.png).

**Part 4: chemical equilibrium**
- With K = 15.6 and 1 mol each of H2 and I2, I solved (2x)^2/((1-x)^2) - K = 0 two ways. Newton (root-finding) gave x = 0.66385 and SLSQP (minimizing the squared imbalance) gave x = 0.66385, so the two methods agree.
- Equilibrium composition: H2 = 0.336 mol, I2 = 0.336 mol, HI = 1.328 mol. The plot (equilibrium.png) shows the reactants falling and the product rising with the extent x, with the equilibrium marked.

**Part 5 (bonus): titration equivalence point**
- I computed the slope of the pH curve with np.gradient(pH, V) and took the volume where it is largest (np.argmax). The equivalence point is at 50.0 mL, where the pH jumps sharply and the slope has its peak (titration.png).