#!/usr/bin/env python3
"""
Three-stage ghost-imaging figure for a blog post.

Figure 3. Making the ghost classical.
Three stages of ghost imaging:
    Left: entangled photon pairs and two detectors.
    Centre: classically correlated speckle beams and two detectors.
    Right: computational ghost imaging — a projector, one fixed detector,
           and a computer.

The script produces a clean three-panel scientific diagram using matplotlib only.

Outputs:
    ghost_imaging_three_stages.png
    ghost_imaging_three_stages.pdf

Usage:
    python ghost_imaging_three_stages.py
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Rectangle,
    FancyBboxPatch,
    Ellipse,
    Circle,
    FancyArrowPatch,
    Polygon,
)


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

FIGSIZE = (15, 5.9)
DPI = 220

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_PNG = SCRIPT_DIR / "ghost_imaging_three_stages.png"
OUT_PDF = SCRIPT_DIR / "ghost_imaging_three_stages.pdf"

FONT_SMALL = 9.5
FONT_LABEL = 11.5
FONT_PANEL = 13.5
FONT_TITLE = 14.5

COLOR_Q = "tab:purple"
COLOR_A = "tab:red"
COLOR_B = "tab:blue"
COLOR_CLASSICAL = "tab:green"
COLOR_COMP = "tab:orange"
COLOR_LINE = "0.18"
COLOR_LIGHT = "0.80"
COLOR_PANEL_BG = "0.985"

LW_BEAM = 2.3
LW_EDGE = 1.2


# ---------------------------------------------------------------------
# Basic drawing helpers
# ---------------------------------------------------------------------

def add_arrow(ax, start, end, color=COLOR_LINE, lw=1.8, mutation_scale=13, zorder=4):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=mutation_scale,
            linewidth=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
            zorder=zorder,
        )
    )


def add_beam(ax, start, end, color, lw=LW_BEAM, alpha=0.95, zorder=2):
    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color=color,
        linewidth=lw,
        alpha=alpha,
        solid_capstyle="round",
        zorder=zorder,
    )


def add_panel_box(ax, x, y, w, h, title):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.03,rounding_size=0.05",
            facecolor=COLOR_PANEL_BG,
            edgecolor="0.84",
            linewidth=1.0,
            zorder=0,
        )
    )
    ax.text(
        x + w / 2,
        y + h - 0.20,
        title,
        ha="center",
        va="top",
        fontsize=FONT_PANEL,
        weight="bold",
        color="0.15",
        zorder=10,
    )


def add_spdc_crystal(ax, center, width=0.30, height=0.70):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width,
            height,
            facecolor="0.93",
            edgecolor=COLOR_Q,
            linewidth=1.3,
            zorder=6,
        )
    )
    ax.plot(
        [x - width / 2, x, x + width / 2],
        [y + height / 2, y + height * 0.66, y + height / 2],
        color=COLOR_Q,
        linewidth=1.0,
        zorder=7,
    )


def add_ground_glass(ax, center, width=0.30, height=0.72):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width,
            height,
            facecolor="0.92",
            edgecolor=COLOR_CLASSICAL,
            linewidth=1.3,
            zorder=6,
        )
    )
    # speckly texture
    rng = np.random.default_rng(1234)
    xs = rng.uniform(x - width / 2 + 0.02, x + width / 2 - 0.02, 45)
    ys = rng.uniform(y - height / 2 + 0.02, y + height / 2 - 0.02, 45)
    ax.scatter(xs, ys, s=4, color=COLOR_CLASSICAL, alpha=0.7, zorder=7)


def add_double_slit(ax, center, width=0.28, height=0.78, slit_width=0.045, gap=0.045):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width,
            height,
            facecolor="0.07",
            edgecolor="0.07",
            zorder=7,
        )
    )
    slit_h = height * 0.72
    slit_y = y - slit_h / 2
    for sx in (x - gap / 2 - slit_width, x + gap / 2):
        ax.add_patch(
            Rectangle(
                (sx, slit_y),
                slit_width,
                slit_h,
                facecolor="white",
                edgecolor="white",
                zorder=8,
            )
        )


def add_fixed_detector(ax, center, scale=1.0):
    x, y = center
    w, h = 0.42 * scale, 0.44 * scale
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor="0.78",
            edgecolor="0.15",
            linewidth=1.2,
            zorder=6,
        )
    )
    ax.add_patch(
        Ellipse(
            (x - w / 2, y),
            width=0.12 * scale,
            height=0.32 * scale,
            facecolor="0.55",
            edgecolor="0.15",
            linewidth=1.0,
            zorder=7,
        )
    )


def add_camera(ax, center, scale=1.0):
    x, y = center
    body_w, body_h = 0.58 * scale, 0.40 * scale
    ax.add_patch(
        FancyBboxPatch(
            (x - body_w / 2, y - body_h / 2),
            body_w,
            body_h,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor="0.28",
            edgecolor="0.10",
            linewidth=1.2,
            zorder=6,
        )
    )
    ax.add_patch(
        Rectangle(
            (x - body_w / 2 - 0.08 * scale, y - 0.16 * scale),
            0.10 * scale,
            0.32 * scale,
            facecolor="0.88",
            edgecolor="0.15",
            linewidth=1.0,
            zorder=7,
        )
    )
    ax.add_patch(
        Rectangle(
            (x - 0.10 * scale, y + body_h / 2 - 0.02 * scale),
            0.20 * scale,
            0.09 * scale,
            facecolor="0.18",
            edgecolor="0.1",
            linewidth=1.0,
            zorder=6,
        )
    )


def add_laptop(ax, center, scale=1.0):
    x, y = center
    screen_w, screen_h = 0.58 * scale, 0.40 * scale
    ax.add_patch(
        Rectangle(
            (x - screen_w / 2, y - screen_h / 2 + 0.05 * scale),
            screen_w,
            screen_h,
            facecolor="0.85",
            edgecolor="0.18",
            linewidth=1.2,
            zorder=6,
        )
    )
    ax.add_patch(
        Rectangle(
            (x - screen_w / 2 + 0.04 * scale, y - screen_h / 2 + 0.09 * scale),
            screen_w - 0.08 * scale,
            screen_h - 0.12 * scale,
            facecolor="0.95",
            edgecolor="0.8",
            linewidth=0.8,
            zorder=7,
        )
    )
    base = Polygon(
        [
            (x - 0.38 * scale, y - 0.18 * scale),
            (x + 0.38 * scale, y - 0.18 * scale),
            (x + 0.28 * scale, y - 0.28 * scale),
            (x - 0.28 * scale, y - 0.28 * scale),
        ],
        closed=True,
        facecolor="0.75",
        edgecolor="0.20",
        linewidth=1.1,
        zorder=5,
    )
    ax.add_patch(base)


def add_projector(ax, center, scale=1.0):
    x, y = center
    w, h = 0.56 * scale, 0.30 * scale
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor="0.82",
            edgecolor="0.15",
            linewidth=1.2,
            zorder=6,
        )
    )
    ax.add_patch(
        Circle(
            (x + w / 2 - 0.08 * scale, y),
            radius=0.07 * scale,
            facecolor="0.55",
            edgecolor="0.15",
            linewidth=1.0,
            zorder=7,
        )
    )


def add_beam_splitter(ax, center, size=0.24):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - size / 2, y - size / 2),
            size,
            size,
            angle=45,
            facecolor="0.90",
            edgecolor="0.40",
            linewidth=1.1,
            zorder=6,
        )
    )


def add_small_ghost_image(ax, xy, size=(0.66, 0.52), label="ghost image"):
    x, y = xy
    w, h = size
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.04",
            facecolor="0.95",
            edgecolor="0.60",
            linewidth=0.9,
            zorder=2,
        )
    )
    # stylized double-slit-like fringe image
    xs = np.linspace(-1, 1, 160)
    ys = np.linspace(-1, 1, 120)
    X, Y = np.meshgrid(xs, ys)
    pattern = np.exp(-(X**2 + Y**2) * 1.8) * (0.5 + 0.5 * np.cos(11 * X)) * (0.3 + 0.7 * np.exp(-Y**2 * 5))
    ax.imshow(
        pattern,
        extent=(x + 0.05, x + w - 0.05, y + 0.07, y + h - 0.07),
        cmap="Blues",
        interpolation="bilinear",
        origin="lower",
        zorder=3,
        alpha=0.95,
        aspect="auto",
    )
    ax.text(
        x + w / 2,
        y - 0.08,
        label,
        ha="center",
        va="top",
        fontsize=FONT_SMALL,
        color="0.25",
        zorder=10,
    )


def add_panel_footer(ax, x, y, w, text):
    ax.text(
        x + w / 2,
        y,
        text,
        ha="center",
        va="top",
        fontsize=FONT_SMALL,
        color="0.25",
        style="italic",
        wrap=True,
    )


# ---------------------------------------------------------------------
# Panel content
# ---------------------------------------------------------------------

def draw_quantum_panel(ax, x0, y0, w, h):
    add_panel_box(ax, x0, y0, w, h, "Entangled photons")

    crystal = (x0 + 0.7, y0 + 2.20)
    slit = (x0 + 2.6, y0 + 2.55)
    fixed = (x0 + 3.6, y0 + 2.55)
    camera = (x0 + 3.6, y0 + 1.55)

    # Pump + crystal
    #add_arrow(ax, (x0 + 0.20, y0 + 2.20), (x0 + 0.72, y0 + 2.20), color=COLOR_Q, lw=2.6)
    #add_beam(ax, (x0 + 0.72, y0 + 2.20), (x0 + 0.95, y0 + 2.20), COLOR_Q, lw=2.6, alpha=0.55)
    #ax.text(x0 + 0.22, y0 + 2.46, "UV", color=COLOR_Q, fontsize=FONT_SMALL + 0.5, ha="left")
    add_spdc_crystal(ax, crystal)
    ax.text(crystal[0], crystal[1] + 0.58, "SPDC", ha="center", fontsize=FONT_SMALL)

    # Two arms
    add_beam(ax, crystal, (fixed[0] - 0.05, fixed[1]), COLOR_A)
    add_beam(ax, crystal, (camera[0] - 0.05, camera[1]), COLOR_B)

    add_double_slit(ax, slit)
    ax.text(slit[0], slit[1] + 0.55, "double slit", ha="center", fontsize=FONT_SMALL)
    add_fixed_detector(ax, fixed)
    add_camera(ax, camera)

    ax.text(fixed[0], fixed[1] + 0.45, "fixed,\nnon-imaging", ha="center", fontsize=FONT_SMALL)
    ax.text(camera[0], camera[1] - 0.48, "camera", ha="center", fontsize=FONT_SMALL)

    # # Coincidence box
    # corr_x, corr_y = x0 + 4.95, y0 + 2.05
    # ax.add_patch(
    #     FancyBboxPatch(
    #         (corr_x - 0.55, corr_y - 0.23),
    #         1.10,
    #         0.46,
    #         boxstyle="round,pad=0.02,rounding_size=0.05",
    #         facecolor="0.98",
    #         edgecolor=COLOR_Q,
    #         linewidth=1.2,
    #         zorder=5,
    #     )
    # )
    # ax.text(corr_x, corr_y + 0.04, "coincidence", ha="center", va="center",
    #         fontsize=FONT_SMALL, weight="bold", color=COLOR_Q)
    # ax.text(corr_x, corr_y - 0.10, "correlation", ha="center", va="center",
    #         fontsize=FONT_SMALL, color=COLOR_Q)

    #add_arrow(ax, (fixed[0] + 0.26, fixed[1]), (corr_x - 0.58, corr_y + 0.10), color="0.25", lw=1.4)
    #add_arrow(ax, (camera[0] + 0.30, camera[1]), (corr_x - 0.58, corr_y - 0.10), color="0.25", lw=1.4)

    # add_small_ghost_image(ax, (x0 + 4.55, y0 + 0.42))
    add_panel_footer(ax, x0, y0 + 0.22, w, "Two photons, two detectors, one image in their correlations")


def draw_classical_panel(ax, x0, y0, w, h):
    add_panel_box(ax, x0, y0, w, h, "Classical speckle")

    laser = (x0 + 0.48, y0 + 2.20)
    diffuser = (x0 + 0.7, y0 + 2.20)
    bs = (x0 + 2.10, y0 + 2.10)
    slit = (x0 + 2.6, y0 + 2.55)
    fixed = (x0 + 3.6, y0 + 2.55)
    camera = (x0 + 3.6, y0 + 1.55)

    # # Laser
    # add_arrow(ax, (laser[0] - 0.28, laser[1]), (laser[0] + 0.10, laser[1]), color=COLOR_CLASSICAL, lw=2.6)
    # ax.text(laser[0] - 0.32, laser[1] + 0.26, "laser", fontsize=FONT_SMALL, color=COLOR_CLASSICAL, ha="left")

    # Rotating diffuser / ground glass
    add_ground_glass(ax, diffuser)
    ax.text(diffuser[0], diffuser[1] + 0.60, "speckle pattern", ha="center", fontsize=FONT_SMALL)

    # Beam to beam splitter
    # add_beam(ax, (laser[0] + 0.10, laser[1]), (diffuser[0] - 0.17, diffuser[1]), COLOR_CLASSICAL, lw=2.4, alpha=0.6)
    # add_beam(ax, (diffuser[0] + 0.17, diffuser[1]), (bs[0] - 0.05, bs[1]), COLOR_CLASSICAL, lw=2.4, alpha=0.75)

    # Beam splitter
    #add_beam_splitter(ax, bs)
    #ax.text(bs[0], bs[1] - 0.50, "beam splitter", ha="center", fontsize=FONT_SMALL)

    # Split beams
    add_beam(ax, (diffuser[0] + 0.17, diffuser[1]), (fixed[0] - 0.05, fixed[1]), COLOR_A)
    add_beam(ax, (diffuser[0] + 0.17, diffuser[1]), (camera[0] - 0.05, camera[1]), COLOR_B)

    add_double_slit(ax, slit)
    ax.text(slit[0], slit[1] + 0.55, "double slit", ha="center", fontsize=FONT_SMALL)
    add_fixed_detector(ax, fixed)
    add_camera(ax, camera)
    ax.text(fixed[0], fixed[1] + 0.45, "fixed,\nnon-imaging", ha="center", fontsize=FONT_SMALL)
    ax.text(camera[0], camera[1] - 0.48, "camera", ha="center", fontsize=FONT_SMALL)

    # # correlation / computer block
    # corr_x, corr_y = x0 + 5.00, y0 + 2.05
    # ax.add_patch(
    #     FancyBboxPatch(
    #         (corr_x - 0.52, corr_y - 0.23),
    #         1.04,
    #         0.46,
    #         boxstyle="round,pad=0.02,rounding_size=0.05",
    #         facecolor="0.98",
    #         edgecolor=COLOR_CLASSICAL,
    #         linewidth=1.2,
    #         zorder=5,
    #     )
    # )
    # ax.text(corr_x, corr_y + 0.02, "correlate", ha="center", va="center",
    #         fontsize=FONT_SMALL, weight="bold", color=COLOR_CLASSICAL)
    # add_arrow(ax, (fixed[0] + 0.26, fixed[1]), (corr_x - 0.54, corr_y + 0.10), color="0.25", lw=1.4)
    # add_arrow(ax, (camera[0] + 0.30, camera[1]), (corr_x - 0.54, corr_y - 0.10), color="0.25", lw=1.4)

    # add_small_ghost_image(ax, (x0 + 4.58, y0 + 0.42))
    add_panel_footer(ax, x0, y0 + 0.22, w, "Random speckle patterns replace entanglement")


def draw_computational_panel(ax, x0, y0, w, h):
    add_panel_box(ax, x0, y0, w, h, "Computational")

    projector = (x0 + 0.70, y0 + 2.05)
    slit = (x0 + 2.05, y0 + 2.05)
    fixed = (x0 + 3.40, y0 + 2.05)
    laptop = (x0 + 3.40, y0 + 0.85)

    add_projector(ax, projector)
    ax.text(projector[0], projector[1] + 0.43, "projector", ha="center", fontsize=FONT_SMALL)

    # Structured-illumination beam
    add_beam(ax, (projector[0] + 0.30, projector[1]), (slit[0] - 0.15, slit[1]), COLOR_COMP, lw=2.5)

    # Optional structured pattern cue: dotted modulation spots
    xs = np.linspace(projector[0] + 0.35, slit[0] - 0.30, 8)
    ys = projector[1] + 0.10 * np.sin(np.linspace(0, 2*np.pi, xs.size))
    ax.scatter(xs, ys, s=10, color=COLOR_COMP, alpha=0.7, zorder=4)

    add_double_slit(ax, slit)
    ax.text(slit[0], slit[1] + 0.55, "double slit", ha="center", fontsize=FONT_SMALL)

    add_beam(ax, (slit[0] + 0.15, slit[1]), (fixed[0] - 0.25, fixed[1]), COLOR_A, lw=2.2)
    add_fixed_detector(ax, fixed)
    ax.text(fixed[0], fixed[1] + 0.45, "fixed,\nnon-imaging", ha="center", fontsize=FONT_SMALL)

    # Laptop / computer
    add_laptop(ax, laptop)
    ax.text(laptop[0], laptop[1] - 0.50, "computer", ha="center", fontsize=FONT_SMALL)

    # Connections
    add_arrow(ax, (fixed[0], fixed[1]-0.3), (laptop[0], laptop[1] + 0.3), color="0.25", lw=1.4)
    #ax.text(x0 + 3.95, y0 + 2.56, "known patterns", fontsize=FONT_SMALL, color=COLOR_COMP, ha="center")
    # add_arrow(ax, (projector[0] + 0.05, projector[1] - 0.30), (laptop[0], laptop[1]), color=COLOR_COMP, lw=1.2)

    #add_small_ghost_image(ax, (x0 + 4.50, y0 + 0.42))
    add_panel_footer(ax, x0, y0 + 0.22, w, "The second optical arm becomes a calculation")


# ---------------------------------------------------------------------
# Main figure
# ---------------------------------------------------------------------

def make_figure():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    ax.set_xlim(0, 15.0)
    ax.set_ylim(0, 5.9)
    ax.axis("off")

    ax.text(
        7.5,
        5.65,
        "Making the ghost classical",
        ha="center",
        va="center",
        fontsize=FONT_TITLE,
        weight="bold",
        color="0.15",
    )

    ax.text(
        7.5,
        5.40,
        "The same image survives while the hardware grows steadily less mysterious.",
        ha="center",
        va="center",
        fontsize=FONT_LABEL,
        color="0.35",
    )

    y0 = 0.50
    w = 4.55
    h = 4.45
    gap = 0.225

    draw_quantum_panel(ax, 0.35, y0, w, h)
    draw_classical_panel(ax, 0.35 + w + gap, y0, w, h)
    draw_computational_panel(ax, 0.35 + 2 * (w + gap), y0, w, h)

    # progression arrows between panels
    #add_arrow(ax, (4.97, 2.73), (5.28, 2.73), color="0.50", lw=1.6, mutation_scale=13)
    #add_arrow(ax, (9.75, 2.73), (10.06, 2.73), color="0.50", lw=1.6, mutation_scale=13)

    fig.tight_layout(pad=0.2)
    return fig


def main():
    fig = make_figure()
    fig.savefig(OUT_PNG, dpi=DPI, bbox_inches="tight")
    fig.savefig(OUT_PDF, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {OUT_PNG}")
    print(f"Saved {OUT_PDF}")


if __name__ == "__main__":
    main()
