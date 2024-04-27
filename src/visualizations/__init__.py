import matplotlib.pyplot as plt

from src.visualizations.sliders import plot_sliders


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 24
plt.rcParams["mathtext.fontset"] = "stix"


def color_each_ax(axes: list[list[plt.Axes]]) -> None:
    for ax_list in axes:
        for ax in ax_list:
            ax.tick_params(labelleft=False, labelbottom=False, left=False, bottom=False)
            for spine in ax.spines.values():
                spine.set_edgecolor("gray")
                spine.set_linewidth(2)
                spine.set_facecolor("lightgray")


__all__ = ["plot_sliders"]
