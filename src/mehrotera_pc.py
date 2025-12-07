from utils import default_start , np , kkt_residuals ,max_step,solve_newton_step

def ipm_mehrotra(A, b, c, max_iter=50, tau=0.99, tol=1e-8):
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
        r_b_aff, r_c_aff, r_mu_aff = kkt_residuals(A, b, c, x, y, s, 0)
        Δx_aff, Δy_aff, Δs_aff = solve_newton_step(A, b, c, x, y, s, r_b_aff, r_c_aff, r_mu_aff)
        α_aff = min(max_step(x, Δx_aff, 1.0), max_step(s, Δs_aff, 1.0))
        x_aff = x + α_aff * Δx_aff
        s_aff = s + α_aff * Δs_aff
        mu_aff = (x_aff @ s_aff) / n
        σ = (mu_aff / mu)**3 if mu > 0 else 0
        r_b, r_c, _ = kkt_residuals(A, b, c, x, y, s, mu)
        r_mu_corr = x * s + Δx_aff * Δs_aff - σ * mu * e
        Δx, Δy, Δs = solve_newton_step(A, b, c, x, y, s, r_b, r_c, r_mu_corr)
        α = min(max_step(x, Δx, tau), max_step(s, Δs, tau))
        x += α * Δx
        y += α * Δy
        s += α * Δs
    return history
