# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW/Lab.

## Setup
Create the environment for a given lab:
```bash
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc
```

##PW1 - Lab A: Reproducible Foundations
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

What I built:
- Completed `plot.py` using NumPy and Matplotlib to read real observation data and render a side-by-side 1×2 subplot with shared axes against the analytical decay model.
- Wrote a declarative `Snakefile` workflow to automate figure generation.

Data & Comparison:
- The observed data points closely follow the theoretical exponential decay law N(t) = N0 * e^(-λt) with λ = 0.3.
- Random counting fluctuations (noise) are evident in the experimental observation scatter, but the overall rate, curvature, and asymptotic trend align with the analytical curve.

Snakemake Automation:
- The Snakemake pipeline defines a rule mapping `decay_observed.csv` and `plot.py` to `figure.png`. It monitors file modification timestamps, executing only when inputs are modified or when `figure.png` is absent, eliminating redundant re-computation.

---

## PW2 - Lab A: Motion from Tracking Data

What I built:
- analysis.py was created and it prints out mean acceleration and standard deviation of acceleration. Mean acceleration=-8.57968750000008 Std=28.71612572170628. 
The reason for these results is that acceleration is much noisier than position because each derivative subtracts nearby noisy measurements and divides by the small time step (0.1 s), so the noise is magnified, and it happens twice.

- Integrating the noisy acceleration back to velocity and then position gave a result within 0.78 m of the original position (max difference). Integration suppresses noise because random errors partly cancel when summed.
- Figure: motion.png shows smooth position, slightly rough velocity, and very noisy acceleration.

Bonus: 2D trajectory (trajectory.csv)
- The path (x vs y) is a figure-eight that crosses itself near the origin, spanning about ±50 m in both x and y, with small wiggles from measurement noise.
- The speed, computed as sqrt(vx² + vy²) from np.gradient of x and y, oscillates repeatedly between about 8 and 38 m/s, with a period of roughly 5 s. It looks fastest around the crossing in the middle of the eight and slowest near the outer ends of the loops.
- The speed curve is much jerkier than the path, because it comes from a derivative and differentiation amplifies noise, the same effect as in the free-fall data.
- Figure: trajectory.png.