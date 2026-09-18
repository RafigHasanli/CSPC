"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)


# TODO 2: test_matches_law
def test_matches_law():
    N0 = 10_000
    lam = 0.3
    dt = 0.05
    steps = 50

    # Run over multiple random seeds and calculate the mean outcome
    seeds = range(30)
    runs = [simulate(N0, lam, dt=dt, steps=steps, seed=s) for s in seeds]
    mean_counts = np.mean(runs, axis=0)

    # Physical law: N(t) = N0 * exp(-lam * t)
    t = np.arange(steps + 1) * dt
    expected = N0 * np.exp(-lam * t)

    # Compare simulated average with the analytical curve within a relative tolerance
    assert mean_counts == pytest.approx(expected, rel=0.03)
