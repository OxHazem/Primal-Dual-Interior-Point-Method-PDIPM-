from utils import default_start ,max_step , np , plt , SCIPY_AVAILABLE , linprog  ,  kkt_residuals ,solve_newton_step 
from central_path_fixed import ipm_central_fixed
from central_path_adaptive import ipm_central_adaptive
from mehrotera_pc import ipm_mehrotra
from case_studies import case_studies, lp_inequalities_to_standard
from plotting import plot_case_study
def compare_with_scipy(name, c, A_ub, b_ub, history_mehrotra):
    x_hist = history_mehrotra['x'][-1]
    n = c.size
    x_ours = x_hist[:n]
    obj_ours = c @ x_ours
    print(f"\n{name}")
    print("Our Mehrotra x =", x_ours)
    print("Our obj =", obj_ours)
    if not SCIPY_AVAILABLE:
        print("SciPy not available.")
        return
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[(0,None)]*n, method="highs-ipm")
    print("SciPy x =", res.x)
    print("SciPy obj =", res.fun)



for name, c, A_ub, b_ub in case_studies():
    A_eq, b_eq, c_std = lp_inequalities_to_standard(c, A_ub, b_ub)

    hist_fixed = ipm_central_fixed(A_eq, b_eq, c_std, max_iter=40)
    hist_adapt = ipm_central_adaptive(A_eq, b_eq, c_std, max_iter=40)
    hist_meh = ipm_mehrotra(A_eq, b_eq, c_std, max_iter=40)

    histories = {
        "fixed": hist_fixed,
        "adaptive": hist_adapt,
        "mehrotra": hist_meh,
    }

    plot_case_study(name, histories)
    compare_with_scipy(name, c, A_ub, b_ub, hist_meh)



