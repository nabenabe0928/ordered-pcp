from __future__ import annotations

from fast_pareto import is_pareto_front2d

import numpy as np

import optuna

import pandas as pd


class Objective:
    def __init__(self):
        self._df_normalized = pd.read_csv("data/normalized_parameter_c_t.csv")
        self._df_raw = pd.read_csv("data/parameter_c_t.csv")
        self._dim = 5
        self._base = 11 ** (self._dim - np.arange(self._dim) - 1)

    def __call__(self, trial: optuna.Trial) -> tuple[float, float]:
        p_indices = [trial.suggest_int(f"p{d}", 0, 10) for d in range(self._dim)]
        index = self._base @ p_indices
        f1 = self._df_normalized["C"][index]
        f2 = self._df_normalized["T"][index]
        return f1, f2


def run_optuna_and_return_pareto_sols(n_trials: int, seed: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    optuna.logging.set_verbosity(optuna.logging.CRITICAL)
    sampler = optuna.samplers.NSGAIISampler(seed=seed)
    study = optuna.create_study(directions=["minimize"]*2, sampler=sampler)
    objective = Objective()
    study.optimize(objective, n_trials=n_trials)

    values = np.array([t.values for t in study.trials])
    on_front = is_pareto_front2d(values)
    pareto_sols = values[on_front]
    order = np.argsort(pareto_sols[:, 0])
    pareto_sols_ordered = pareto_sols[order]
    return values, pareto_sols
