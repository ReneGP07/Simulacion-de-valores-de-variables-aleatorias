
"""Simulación de una variable aleatoria Binomial usando la pseudoinversa de la CDF."""

import math
import random
from typing import List


def binomial_pmf(n: int, p: float, k: int) -> float:
    if k < 0 or k > n:
        return 0.0
    coef = math.comb(n, k)
    return coef * (p ** k) * ((1 - p) ** (n - k))


def binomial_inverse_cdf_sample(n: int, p: float) -> int:
    u = random.random()
    if u == 0.0:
        u = 1e-12

    F = 0.0
    for k in range(0, n + 1):
        F += binomial_pmf(n, p, k)
        if u <= F:
            return k
    return n


def sample_binomial(n: int, p: float, N: int) -> List[int]:
    return [binomial_inverse_cdf_sample(n, p) for _ in range(N)]


if __name__ == "__main__":
    n = 5
    p = 0.3
    N = 20
    datos = sample_binomial(n, p, N)
    print(f"Muestras de X ~ Bin({n}, {p}):", datos)
