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

---

## PW3 - Session 1: Characterising the Data

**What I built:**
- `pw3_session1.py` loads `heart.csv` with pandas, prints the shape and first rows, and isolates the four continuous columns age, chol, trestbps and thalach. The file was generated by `make_heart_csv.py` from `processed.cleveland.data` (Cleveland subset, 303 patients, 14 columns) in the UCI Heart Disease dataset, with `target = 1` for any disease level above 0.
- Source: Janosi, A., Steinbrunn, W., Pfisterer, M., Detrano, R. (1988). *Heart Disease*. UCI Machine Learning Repository. https://archive.ics.uci.edu/dataset/45/heart+disease
- Figure: `fig_distributions.png` shows a histogram, a KDE curve and a fitted normal curve for each variable in four panels. `fig_qq.png` shows a Q-Q plot for each variable.

**Shapes of the distributions:**
- age: broad and bumpy with no clear single peak (highest bar near 58, a dip near 50). Slightly skewed to the left (skew -0.21) and flat-topped. Mean 54.4, and half of the patients are between 48 and 61.
- chol: skewed to the right (skew 1.13) with a long upper tail and heavy tails (excess kurtosis 4.4). Mean 246.7, with one extreme patient at 564 mg/dl.
- trestbps: skewed to the right (skew 0.70), peak around 120 to 140, tail up to 200 mmHg. The histogram is spiky because values cluster on round numbers (120, 130, 140).
- thalach: skewed to the left (skew -0.53), peak around 160 bpm, long tail down to 71 bpm.

**Normality check:**

| variable | skew | excess kurtosis | Shapiro-Wilk p | verdict |
|---|---|---|---|---|
| age | -0.21 | -0.53 | 0.006 | approximately normal |
| chol | 1.13 | 4.40 | <0.0001 | not normal |
| trestbps | 0.70 | 0.85 | <0.0001 | not normal |
| thalach | -0.53 | -0.07 | 0.0001 | not normal (mildly) |

- With n = 303 the tests are very sensitive and reject normality for tiny deviations, so every p-value is below 0.05, including age. Because of this I judged the variables using the Q-Q plots and the size of the skew and kurtosis as well as the p-values (Shapiro-Wilk and D'Agostino-Pearson gave the same conclusions).
- age: the Q-Q plot follows the line closely, with only the extreme ends slightly off (lighter tails than a normal). The skew is small, so I treat it as approximately normal.
- chol: the Q-Q plot bends sharply upward at the right end, with the 564 point far above the line. Removing that outlier lowers the skew to 0.51, but Shapiro-Wilk still rejects (p = 0.001), so the outlier is not the only cause.
- trestbps: the upper tail sits above the line (right skew) and the points form steps because of the round-number values. Not normal.
- thalach: the low end of the Q-Q plot falls below the line (heavy left tail). It is the closest to normal of the three rejected variables, but I still treat it as not normal.

**Consequence for Session 2:** I will use non-parametric methods (Mann-Whitney U, Spearman) for chol, trestbps and thalach. With about 300 patients a t-test on age would also be reasonable.


---

## PW3 - Session 2: Drawing Conclusions

**What I built:**
- `PW3/Session 2/session2.py` runs the whole of Session 2 and writes all numbers to `results.txt`. `heart.csv` was rebuilt from `processed.cleveland.data` exactly as in Session 1 (`target = 1` for any disease level above 0). The chemical-exposure dataset is `chemicals_cancer.csv` (1000 patients: benzene, cadmium, pollution_index, age, malignancy).
- Figures: `thalach_means.png` (mean thalach with 95% CI), `age_thalach.png` (scatter) and `chemicals.png` (malignancy vs benzene and vs cadmium, coloured by pollution).

**4. Is the effect real? (thalach, disease vs healthy)**
- Method: thalach is not normal (Session 1), so I used the Mann-Whitney U test, which compares the two groups without assuming normality. As a cross-check I also ran Welch's t-test, which does not assume equal variances.
- Result: U = 5806.5, p = 1.9e-13 (Welch: t = -7.86, p = 9.1e-14). The p-value is far below 0.05, so I reject "same distribution": the two groups differ.
- Effect size: the mean difference is 19.1 bpm. The chance that a random disease patient has a higher thalach than a random healthy patient is U / (n1 n2) = 0.25, so most of the time the disease patient is lower.
- Conclusion: patients with heart disease reach a significantly lower maximum heart rate than healthy ones. Both tests agree.

**Mean with uncertainty (95% confidence interval = mean ± 1.96 × SEM, SEM = s / sqrt(n)):**

| group | n | mean thalach (bpm) | SEM | 95% CI |
|---|---|---|---|---|
| disease | 139 | 139.3 | 1.92 | 135.5 to 143.0 |
| healthy | 164 | 158.4 | 1.50 | 155.4 to 161.3 |

- The plot shows the two means with the 95% CI as error bars. The intervals do not overlap (143.0 < 155.4), so the picture agrees with the test. The CI of a mean is reliable here even though thalach is not perfectly normal, because both groups have well over 100 patients.

**5. Do age and thalach move together?**
- thalach is not normal, so I used the Spearman rank correlation: rho = -0.39, p = 1.5e-12. Pearson gives the same answer (r = -0.39, p = 1.1e-12).
- Interpretation: older patients tend to reach a lower maximum heart rate. The relationship is moderate (about 15% of the variance), and the scatter plot shows a clear downward trend with a lot of spread around it.

**6. Naive analysis (chemicals)**
- Correlation with malignancy: cadmium r = 0.88, benzene r = 0.385. Taken at face value, cadmium looks like the cause.

**7. Look again (confounding)**
- Suspected third variable: pollution_index. It correlates with cadmium at r = 0.98 and with malignancy at r = 0.90, but almost not at all with benzene (r = 0.05). So pollution moves with both cadmium and malignancy, which is what a confounder does.
- I recomputed the associations in three ways: restricting to patients with similar pollution (40th to 60th percentile, n = 200), splitting into 5 pollution bins, and a partial correlation (removing the linear effect of pollution from both variables).

| chemical | naive r | restricted (similar pollution) | per-bin range | partial r |
|---|---|---|---|---|
| benzene | 0.385 | 0.70 | 0.67 to 0.74 | 0.76 |
| cadmium | 0.88 | 0.31 | 0.19 to 0.31 | 0.01 |

- Benzene is the real cause of malignancy. Its association gets stronger once pollution is held fixed, and it stays at about 0.7 in every bin. Pollution was adding variation to malignancy that benzene does not explain, which hid benzene's effect in the naive analysis.
- Cadmium only looked guilty. It follows pollution almost perfectly, so it acted as a proxy for it. When pollution is accounted for, its association falls from 0.88 to about 0 (partial r = 0.01). The restricted value of 0.31 is not zero only because the 40-60 percentile window still contains some pollution variation; the partial correlation removes that.
- This shows the difference between correlation and causation: the strongest correlation (cadmium) was not the cause, and the weaker one (benzene) was. The conclusion rests on this dataset and on one controlled variable (pollution), but the result is consistent across all three methods.

**Bonus: how unpredictable is the target?**
- Proportions: 54.1% healthy (0), 45.9% disease (1). Shannon entropy H = -sum(p log2 p) = 0.995 bits, where 1 bit is the maximum for two categories. The column is almost perfectly balanced, so it is about as hard to guess as a binary column can be (always guessing "healthy" is right only 54% of the time).
