import time
from decay import simulate, simulate_loop

def benchmark():
    N0 = 200_000
    lam = 0.2
    dt = 0.05
    steps = 50

    print(f"Benchmarking radioactive decay (N0 = {N0:,}, steps = {steps})...\n")

    # Time pure-Python loop
    t0 = time.perf_counter()
    simulate_loop(N0, lam, dt=dt, steps=steps, seed=42)
    t_loop = time.perf_counter() - t0

    # Time NumPy vectorized version
    t1 = time.perf_counter()
    simulate(N0, lam, dt=dt, steps=steps, seed=42)
    t_numpy = time.perf_counter() - t1

    speedup = t_loop / t_numpy

    print(f"simulate_loop (pure Python) : {t_loop:.4f} s")
    print(f"simulate      (NumPy)       : {t_numpy:.6f} s")
    print(f"Speed-up factor             : {speedup:.1f}x faster")

if __name__ == "__main__":
    benchmark() 