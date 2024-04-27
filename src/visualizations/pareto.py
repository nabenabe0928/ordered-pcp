from __future__ import annotations

import matplotlib.pyplot as plt

import numpy as np

from src.weight_calculator import fit_and_return_params
from src.weight_calculator import hyperbolic_curve


def set_color_bar(scatter_object: plt.Line2D) -> None:
    cax = plt.axes((0.425, 0.57, 0.01, 0.25))
    cbar = plt.colorbar(scatter_object, orientation="vertical", cax=cax)
    cbar.ax.set_xlabel(r'$E$', fontsize=18)
    cbar.ax.tick_params(labelsize=14)


def plot_pareto(ax: plt.Axes, values: np.ndarray, weight: float, slider_value_range: tuple[float, float]) -> None:
    E = weight * values[:, 0] + (1 - weight) * values[:, 1]
    sols_of_interest = (slider_value_range[0] <= E) & (E <= slider_value_range[1])
    ax.set_xlabel("Congestion ($f_1$)")
    ax.set_ylabel("Evacuation Time ($f_2$)")

    good_values = values[sols_of_interest]
    bad_values = values[~sols_of_interest]
    good_E = E[sols_of_interest]
    vmin, vmax = slider_value_range
    line = ax.scatter(
        good_values[:, 0], good_values[:, 1], s=1, c=good_E, cmap=plt.get_cmap("viridis"), vmin=vmin, vmax=vmax
    )
    ax.scatter(bad_values[:, 0], bad_values[:, 1], s=1, color="gray")
    ax.grid()
    set_color_bar(line)


def plot_tangential_line(ax: plt.Axes, x_target: float, pareto_sols: np.ndarray) -> plt.Line2D:
    a, b = fit_and_return_params(pareto_sols)
    slope = - a / (x_target + b) ** 2
    dx = np.linspace(- b + 1e-3, 1, 200)
    y_target = hyperbolic_curve(np.array([x_target]), a, b)[0]
    return ax.plot(dx, slope * (dx - x_target) + y_target, color="olive")


def plot_fitted_curve(ax: plt.Axes, pareto_sols: np.ndarray) -> None:
    a, b = fit_and_return_params(pareto_sols)
    dx = np.linspace(- b + 1e-3, 1.0, 200)
    ax.plot(dx, hyperbolic_curve(dx, a, b), color="black", linestyle="--")


def plot_pareto_with_tangential_line(
    fig: plt.Figure,
    ax: plt.Axes,
    values: np.ndarray,
    pareto_sols: np.ndarray,
    x_target: float,
    weight: float,
    slider_value_range: tuple[float, float],
) -> None:
    a, b = fit_and_return_params(pareto_sols)
    ax = fig.add_axes([0.17, 0.57, 0.25, 0.25])
    ax.tick_params(labelbottom=False, bottom=False, labelleft=False, left=False)
    ax.set_title("Pareto Front")
    plot_pareto(ax, values, weight=weight, slider_value_range=slider_value_range)
    plot_fitted_curve(ax, pareto_sols)
    plot_tangential_line(ax, x_target=x_target, pareto_sols=pareto_sols)
