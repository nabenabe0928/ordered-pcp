from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
from matplotlib.widgets import RangeSlider
from matplotlib.widgets import Slider


def get_range_slider(
    label: str, position_y: float, valinit: list[int] | None = None, valstep: float = 0.1
) -> RangeSlider:
    ax = plt.axes([0.155, position_y, 0.2, 0.01])
    valinit = valinit if valinit is not None else [0, 1]
    range_slider = RangeSlider(ax, label, 0, 1, valinit=valinit, valstep=valstep)
    return range_slider


def plot_sliders(fig: plt.Figure, ax: plt.Axes) -> list[RangeSlider]:
    ax.set_title("Settings", y=0.85)
    position_y = 0.37
    step_y = 0.04
    ax = fig.add_axes([0.155, position_y, 0.2, 0.01])
    position_y -= step_y
    handle_style = dict(facecolor='black', edgecolor='.75', size=10)
    slider = Slider(ax=ax, label="$w_1$", valmin=0, valmax=1.0, valinit=0.5, valstep=0.01, handle_style=handle_style)
    labels = [f"$\lambda_{i}$" for i in range(1, 6)]
    range_sliders = [slider, get_range_slider("$E$", position_y, valinit=[0.0, 0.1], valstep=0.01)]
    position_y -= step_y
    range_sliders += [get_range_slider(label, position_y - i * step_y) for i, label in enumerate(labels)]
    return range_sliders
