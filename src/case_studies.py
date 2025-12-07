import numpy as np
def lp_inequalities_to_standard(c, A_ub, b_ub):
    m, n = A_ub.shape
    A_eq = np.hstack([A_ub, np.eye(m)])
    b_eq = b_ub.copy()
    c_std = np.concatenate([c, np.zeros(m)])
    return A_eq, b_eq, c_std

def case_studies():
    c1 = np.array([-3., -1.])
    A1 = np.array([[1., 1.], [2., 1.]])
    b1 = np.array([4., 5.])

    c2 = np.array([-2., -4.])
    A2 = np.array([[1., 2.], [3., 1.]])
    b2 = np.array([8., 9.])

    c3 = np.array([-1., -2., -3.] )
    A3 = np.array([[1., 1., 1.], [2., 2., 1.], [0., 1., 3.]])
    b3 = np.array([10., 15., 12.])

    return [
        ("Case 1 (2D)", c1, A1, b1),
        ("Case 2 (2D)", c2, A2, b2),
        ("Case 3 (3D)", c3, A3, b3),
    ]
