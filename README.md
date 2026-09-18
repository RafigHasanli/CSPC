# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW/Lab.

## Setup
Create the environment for a given lab:
```bash
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc
PW1 - Lab A: Reproducible Foundations
What I built:

Created the personal course repository structure, isolated conda environment, git version control history, automated pytest suite, and performance benchmark script for radioactive decay.

Speed comparison (loop vs NumPy):

loop : 1.3147 s

numpy : 0.0002 s

speed-up: 7435.6 x faster

Tests: all passing? yes

Conclusion:

Vectorizing the simulation with NumPy replaces explicit Python loops with compiled C routines, yielding an acceleration of over 7,400x on 200,000 atoms. Integrating pytest validates statistical outputs against the analytical exponential decay law, and maintaining environment specifications ensures identical behavior across systems.
