#!/usr/bin/env python3
"""Feature image for the ghost-imaging article.

Based on Figure_1_generator.py, but simplified for a Medium feature image.
It keeps the ghost-interference schematic and adds the editorial hook:

    How can the camera record the interference fringes
    if the photon it detects never passes through the slits?

Outputs:
    Feature_image.png
    Feature_image.pdf
"""

from __future__ import annotations

from pathlib import Path
import textwrap

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path as MplPath


# =============================================================================
# SETTINGS
# =============================================================================

FIGSIZE = (14, 6.4)
DPI = 220

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_PNG = SCRIPT_DIR / "Feature_image.png"
OUT_PDF = SCRIPT_DIR / "Feature_image.pdf"

FONT_SCALE = 1.4
FONT_SMALL = 10.0 * FONT_SCALE
FONT_LABEL = 11.0 * FONT_SCALE
FONT_QUESTION = 18.0 * FONT_SCALE

QUESTION = (
    "How can a camera see interference from a photon "
    "that never passed through the slits?"
)
QUESTION_WRAP = 46

PATH_LW = 2.3
BEAM_LW = 2.7

COLOR_PUMP = "tab:purple"
COLOR_A = "tab:red"
COLOR_B = "tab:blue"
COLOR_NEUTRAL = "0.22"
COLOR_BACKGROUND = "white"


# =============================================================================
# DRAWING HELPERS
# =============================================================================

def add_arrow(ax, start, end, color=COLOR_NEUTRAL, lw=PATH_LW,
              mutation_scale=14, zorder=3):
    ax.add_patch(
        FancyArrowPatch(
            start, end,
            arrowstyle="-|>",
            mutation_scale=mutation_scale,
            linewidth=lw,
            color=color,
            shrinkA=0,
            shrinkB=0,
            zorder=zorder,
        )
    )


def add_beam(ax, start, end, color, lw=BEAM_LW, alpha=0.9, zorder=2):
    ax.plot(
        [start[0], end[0]],
        [start[1], end[1]],
        color=color,
        linewidth=lw,
        alpha=alpha,
        solid_capstyle="round",
        zorder=zorder,
    )


def add_spdc_crystal(ax, center, width=0.42, height=0.90):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width, height,
            linewidth=1.4,
            edgecolor=COLOR_PUMP,
            facecolor="0.93",
            zorder=6,
        )
    )
    ax.plot(
        [x - width / 2, x, x + width / 2],
        [y + height / 2, y + height * 0.68, y + height / 2],
        color=COLOR_PUMP,
        linewidth=1.0,
        alpha=0.8,
        zorder=7,
    )


def add_double_slit(ax, center, width=0.42, height=1.05,
                    slit_width=0.07, gap=0.08):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width, height,
            facecolor="0.08",
            edgecolor="0.08",
            zorder=7,
        )
    )
    slit_h = height * 0.72
    slit_y = y - slit_h / 2
    for slit_x in (x - gap / 2 - slit_width, x + gap / 2):
        ax.add_patch(
            Rectangle(
                (slit_x, slit_y),
                slit_width, slit_h,
                facecolor="white",
                edgecolor="white",
                zorder=8,
            )
        )


def add_fixed_detector(ax, center, scale=1.0):
    x, y = center
    w, h = 0.52 * scale, 0.55 * scale
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w, h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor="0.78",
            edgecolor="0.15",
            linewidth=1.3,
            zorder=6,
        )
    )
    ax.add_patch(
        Ellipse(
            (x - w / 2, y),
            width=0.16 * scale,
            height=0.42 * scale,
            facecolor="0.55",
            edgecolor="0.15",
            linewidth=1.1,
            zorder=7,
        )
    )


def add_camera(ax, center, scale=1.0):
    x, y = center
    body_w, body_h = 0.74 * scale, 0.48 * scale
    ax.add_patch(
        FancyBboxPatch(
            (x - body_w / 2, y - body_h / 2),
            body_w, body_h,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor="0.25",
            edgecolor="0.1",
            linewidth=1.3,
            zorder=6,
        )
    )
    ax.add_patch(
        Rectangle(
            (x - body_w / 2 - 0.10 * scale, y - 0.20 * scale),
            0.12 * scale, 0.40 * scale,
            facecolor="0.88",
            edgecolor="0.15",
            linewidth=1.1,
            zorder=7,
        )
    )
    ax.add_patch(
        Rectangle(
            (x - 0.12 * scale, y + body_h / 2 - 0.02 * scale),
            0.24 * scale, 0.10 * scale,
            facecolor="0.18",
            edgecolor="0.1",
            linewidth=1.0,
            zorder=6,
        )
    )


def add_correlation_box(ax, center, width=1.72, height=0.72):
    x, y = center
    ax.add_patch(
        FancyBboxPatch(
            (x - width / 2, y - height / 2),
            width, height,
            boxstyle="round,pad=0.03,rounding_size=0.08",
            facecolor="0.98",
            edgecolor=COLOR_PUMP,
            linewidth=1.7,
            zorder=5,
        )
    )
    ax.text(
        x, y + 0.08, "Coincidence",
        ha="center", va="center",
        fontsize=FONT_LABEL,
        weight="bold",
        color=COLOR_PUMP,
        zorder=6,
    )
    ax.text(
        x, y - 0.14, "correlation",
        ha="center", va="center",
        fontsize=FONT_LABEL,
        color=COLOR_PUMP,
        zorder=6,
    )


def add_curved_wire(ax, start, end, color="0.15", lw=1.8, bend=0.35):
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    vertices = [
        (x0, y0),
        (x0 + bend * dx, y0),
        (x1 - bend * dx, y1),
        (x1, y1),
    ]
    codes = [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4]
    ax.add_patch(
        PathPatch(
            MplPath(vertices, codes),
            facecolor="none",
            edgecolor=color,
            linewidth=lw,
            zorder=3,
        )
    )


def add_fringe_icon(ax, center, width=1.55, height=0.78):
    x0, y0 = center
    left = x0 - width / 2
    bottom = y0 - height / 2

    ax.add_patch(
        FancyBboxPatch(
            (left, bottom),
            width, height,
            boxstyle="round,pad=0.025,rounding_size=0.05",
            facecolor="0.985",
            edgecolor=COLOR_PUMP,
            linewidth=1.2,
            zorder=2,
        )
    )

    xx = np.linspace(-4.0, 4.0, 450)
    envelope = np.sinc(xx / 4.0) ** 2
    fringes = 0.5 * (1 + np.cos(2 * np.pi * xx / 1.32))
    yy = envelope * fringes
    yy /= yy.max()

    xs = left + 0.10 * width + (xx - xx.min()) / (xx.max() - xx.min()) * 0.80 * width
    ys = bottom + 0.16 * height + yy * 0.66 * height
    ax.plot(xs, ys, color=COLOR_PUMP, lw=1.9, zorder=4)


# =============================================================================
# FIGURE
# =============================================================================

def make_figure():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor(COLOR_BACKGROUND)

    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    # -------------------------------------------------------------------------
    # Large, simplified schematic
    # -------------------------------------------------------------------------
    y_source = 4.55
    crystal = (2.20, y_source)

    # Pump and source
    add_arrow(
        ax,
        (0.45, y_source),
        (1.05, y_source),
        color=COLOR_PUMP,
        lw=3.0,
        mutation_scale=16,
    )
    add_beam(
        ax,
        (1.05, y_source),
        (1.98, y_source),
        COLOR_PUMP,
        lw=3.0,
        alpha=0.6,
    )
    add_spdc_crystal(ax, crystal, width=0.48, height=1.00)

    # Upper arm: photon A passes through the double slit.
    slit = (6.35, 5.02)
    fixed = (8.65, 5.15)

    add_beam(ax, crystal, (8.20, 5.15), COLOR_A, lw=3.0)
    add_double_slit(
        ax,
        slit,
        width=0.50,
        height=1.25,
        slit_width=0.085,
        gap=0.10,
    )
    add_fixed_detector(ax, fixed, scale=1.15)

    # Lower arm: photon B goes straight to the camera.
    camera = (8.70, 3.86)

    add_beam(ax, crystal, (8.12, 3.91), COLOR_B, lw=3.0)
    add_camera(ax, camera, scale=1.18)

    # Keep only the labels that matter at thumbnail scale.
    ax.text(
        4.05,
        5.13,
        "Photon A",
        color=COLOR_A,
        fontsize=FONT_LABEL,
        weight="bold",
    )
    ax.text(
        slit[0],
        5.78,
        "double slit",
        ha="center",
        fontsize=FONT_LABEL,
        weight="bold",
    )
    ax.text(
        3.92,
        3.88,
        "Photon B",
        color=COLOR_B,
        fontsize=FONT_LABEL,
        weight="bold",
    )
    ax.text(
        camera[0],
        3.25,
        "camera",
        ha="center",
        fontsize=FONT_LABEL,
        weight="bold",
    )

    # Correlation and interference result.
    corr = (10.60, 4.52)
    fringe = (8.82, 2.52)

    add_correlation_box(ax, corr, width=1.82, height=0.78)
    add_curved_wire(ax, (8.83, 5.18), (9.68, 4.77))
    add_curved_wire(ax, (9.14, 3.91), (9.68, 4.29))

    # add_arrow(
    #     ax,
    #     (11.53, 4.52),
    #     (11.90, 4.52),
    #     color=COLOR_PUMP,
    #     lw=2.0,
    #     mutation_scale=13,
    # )
    add_fringe_icon(ax, fringe, width=1.70, height=0.90)

    # -------------------------------------------------------------------------
    # Editorial hook: large and close to the schematic to avoid dead space.
    # -------------------------------------------------------------------------
    wrapped = "\n".join(textwrap.wrap(QUESTION, width=QUESTION_WRAP))
    ax.text(
        7.0,
        1.18,
        wrapped,
        ha="center",
        va="center",
        fontsize=FONT_QUESTION,
        weight="bold",
        color="0.12",
        linespacing=1.12,
    )

    fig.subplots_adjust(
        left=0.025,
        right=0.985,
        top=0.965,
        bottom=0.035,
    )
    return fig


def main():
    fig = make_figure()
    fig.savefig(OUT_PNG, dpi=DPI, bbox_inches="tight", facecolor=fig.get_facecolor())
    fig.savefig(OUT_PDF, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)

    print(f"Saved {OUT_PNG}")
    print(f"Saved {OUT_PDF}")


if __name__ == "__main__":
    main()
