from utils import default_start , np  , kkt_residuals , solve_newton_step , max_step

def ipm_central_fixed(A, b, c, max_iter=50, alpha_frac=0.99, sigma=0.5, tol=1e-8):
    m, n = A.shape
    x, y, s = default_start(A, b, c)
    e = np.ones(n)
    history = {'obj': [], 'mu': [], 'x': [], 'y': [], 's': []}
    for k in range(max_iter):
        mu = (x @ s) / n
        history['obj'].append(c @ x)
        history['mu'].append(mu)
        history['x'].append(x.copy())
        history['y'].append(y.copy())
        history['s'].append(s.copy())
        r_b, r_c, _ = kkt_residuals(A, b, c, x, y, s, mu)
        if np.linalg.norm(r_b) < tol and np.linalg.norm(r_c) < tol and mu < tol:
            break
        target_mu = sigma * mu
        r_b, r_c, r_mu = kkt_residuals(A, b, c, x, y, s, target_mu * e)
        Δx, Δy, Δs = solve_newton_step(A, b, c, x, y, s, r_b, r_c, r_mu)
        α = min(max_step(x, Δx, alpha_frac), max_step(s, Δs, alpha_frac))
        x += α * Δx
        y += α * Δy
        s += α * Δs
    return history
