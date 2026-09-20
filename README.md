# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW/Lab.

## Setup
Create the environment for a given lab:
```bash
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc

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
- The observed data points closely follow the theoretical exponential decay law $N(t) = N_0 e^{-\lambda t}$ with $\lambda = 0.3$.
- Random counting fluctuations (noise) are evident in the experimental observation scatter, but the overall rate, curvature, and asymptotic trend align with the analytical curve.

Snakemake Automation:
- The Snakemake pipeline defines a rule mapping `decay_observed.csv` and `plot.py` to `figure.png`. It monitors file modification timestamps, executing only when inputs are modified or when `figure.png` is absent, eliminating redundant re-computation.
