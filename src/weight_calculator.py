from __future__ import annotations

from fast_pareto import is_pareto_front2d

import numpy as np

import pandas as pd

from scipy.optimize import curve_fit


def hyperbolic_curve(x: np.ndarray, a: float, b: float) -> np.ndarray:
    return a / (x + b)


def fit_and_return_params(pareto_sols: np.ndarray) -> tuple[float, float]:
    order = np.argsort(pareto_sols[:, 0])
    ordered_pareto_sols = pareto_sols[order]
    X = ordered_pareto_sols[:, 0]
    Y = ordered_pareto_sols[:, 1]
    params_init = (1, 0.5)
    params, _ = curve_fit(hyperbolic_curve, X, Y, p0=params_init)
    a, b = params
    return a, b
