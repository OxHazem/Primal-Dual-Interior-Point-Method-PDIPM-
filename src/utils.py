import numpy as np
import matplotlib.pyplot as plt

try:
    from scipy.optimize import linprog
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False



def max_step(x, dx, tau=0.99):
    idx = dx < 0
    if not np.any(idx):
        return 1.0
    return min(1.0, tau * np.min(-x[idx] / dx[idx]))

def kkt_residuals(A, b, c, x, y, s, mu):
    r_b = A @ x - b
    r_c = A.T @ y + s - c
    r_mu = x * s - mu
    return r_b, r_c, r_mu

def solve_newton_step(A, b, c, x, y, s, r_b, r_c, r_mu):
    S_inv = 1.0 / s
    X = x
    ASX = A * (S_inv * X)[np.newaxis, :]
    M = ASX @ A.T
    rhs = A @ (S_inv * (r_mu - X * r_c)) - r_b
    Δy = np.linalg.solve(M, rhs)
    Δs = -r_c - A.T @ Δy
    Δx = S_inv * (-r_mu - X * Δs)
    return Δx, Δy, Δs

def default_start(A, b, c):
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    x = np.maximum(x, 1.0)
    y = np.linalg.lstsq(A.T, c, rcond=None)[0]
    s = c - A.T @ y
    s = np.maximum(s, 1.0)
    return x, y, s
