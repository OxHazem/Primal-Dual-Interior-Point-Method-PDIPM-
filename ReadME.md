
# README.md (Plain Version)

```markdown
# Primal–Dual Interior Point Methods for Linear Programming  
Math 303 — Report #2

This project implements three classical Primal–Dual Interior Point Methods (IPM) for solving Linear Programming (LP) problems in standard form:

1. Central Path Method with Fixed Step Size and Fixed Centering Parameter  
2. Central Path Method with Adaptive Step Size and Adaptive Centering Parameter  
3. Mehrotra Predictor–Corrector Method  

The purpose of the project is to compare these algorithms across multiple case studies and evaluate the accuracy of the Mehrotra method against SciPy's built-in interior point solver `highs-ipm`.

---

## Project Structure

```

project/
│
├── src/
│   ├── utils.py                     # Shared utilities (residuals, Newton step, max step, initialization)
│   ├── central_path_fixed.py        # Fixed-step primal–dual central path algorithm
│   ├── central_path_adaptive.py     # Adaptive-step primal–dual central path algorithm
│   ├── mehrotra_pc.py               # Mehrotra predictor–corrector implementation
│   ├── case_studies.py              # Defines LP problems and converts inequalities to standard form
│   ├── plotting.py                  # Plots for objectives, central path, and complementarity
│   └── experiments.py               # Runs all solvers and comparisons
│
├── figures/                         # Output plots
│
├── report/
│   ├── report.tex                   # LaTeX report
│   └── report.pdf                   # Final PDF
│
└── README.md

````

---

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd "<your-project-folder>"
````

2. (Optional) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install required packages:

```bash
pip install numpy scipy matplotlib
```

---

## Running the Experiments

Run the experiments from the project root directory:

```bash
python src/experiments.py
```

This script will:

* Convert all LPs to standard form
* Run the three IPM algorithms
* Display plots for each case study:

  * Objective function versus iteration
  * Central path trajectory
  * Complementarity (μ) versus iteration
* Compare the Mehrotra method with SciPy’s `highs-ipm` solver

If SciPy is installed, the terminal output will include:

```
Case 1 (2D)
Our Mehrotra x = [...]
Our objective = ...
SciPy x = [...]
SciPy objective = ...
```

All plots will be displayed using Matplotlib.

---

## Algorithms Implemented

### 1. Central Path Method (Fixed Parameters)

Uses fixed step-size fraction and fixed centering parameter.
Solves the primal–dual Newton system at each iteration.

### 2. Central Path Method (Adaptive Parameters)

Includes an affine-scaling predictor direction and computes:

[
\sigma = (\mu_{\text{aff}} / \mu)^3
]

This improves convergence over the fixed-parameter method.

### 3. Mehrotra Predictor–Corrector

The most advanced method implemented.
It combines:

* An affine predictor direction
* An estimate of the affine complementarity
* Mehrotra’s centering rule
* A corrector direction to maintain centrality

This approach closely matches the design of modern IPM solvers such as HiGHS, MOSEK, and Gurobi.

---

## Case Studies

Three LP problems are included in `case_studies.py`:

1. **Case 1 (2D)**
   Objective:
   [
   \min -3x_1 - x_2
   ]
   Constraints:
   [
   x_1 + x_2 \le 4, \quad 2x_1 + x_2 \le 5
   ]

2. **Case 2 (2D)**
   Objective:
   [
   \min -2x_1 - 4x_2
   ]
   Constraints:
   [
   x_1 + 2x_2 \le 8, \quad 3x_1 + x_2 \le 9
   ]

3. **Case 3 (3D)**
   Objective:
   [
   \min -x_1 - 2x_2 - 3x_3
   ]
   Constraints:
   [
   x_1 + x_2 + x_3 \le 10, \quad 2x_1 + 2x_2 + x_3 \le 15, \quad x_2 + 3x_3 \le 12
   ]

These problems allow comparison of algorithm behavior in different dimensions and geometries.

---

## Output Figures

The following plots are generated for each case study:

* Objective value vs. iteration
* Central path trajectory (for 2D problems)
* Complementarity measure μ vs. iteration

Plots are displayed automatically and can be saved to the `figures/` directory.

---

## Comparison with SciPy

The function `compare_with_scipy()` compares the final result of your Mehrotra implementation with SciPy’s interior-point solver (`highs-ipm`).
This verifies correctness by comparing solution vector and objective value.

---

## Notes

* Always run the code from the project root directory.
* If module import errors occur, set the Python path manually:

```bash
export PYTHONPATH="$PWD/src"
```

* All algorithms use the same initialization and Newton system solver for fairness.

---

## Author

Math 303 — Interior Point Methods Project
Omar Hazem  , Abdelrahman Mohammed
