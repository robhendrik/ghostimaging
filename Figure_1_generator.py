#!/usr/bin/env python3
"""Ghost-imaging far-field schematic for a general-audience blog figure.

Creates the same figure layout as the original script:
- UV laser pumps an SPDC crystal.
- Photon A passes through a double slit and reaches a fixed detector.
- Photon B propagates directly to a position-sensitive camera.
- Both detector signals feed a coincidence/correlation block.
- Lower panels illustrate that neither detector alone contains the final
  interference pattern, while the coincidence correlation does.

Outputs:
    ghost_imaging_far_field_schematic.png
    ghost_imaging_far_field_schematic.pdf
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (
    Ellipse,
    FancyArrowPatch,
    FancyBboxPatch,
    PathPatch,
    Rectangle,
)
from matplotlib.path import Path as MplPath


# =============================================================================
# SETTINGS
# =============================================================================

FIGSIZE = (14, 8.2)
DPI = 220

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_PNG = SCRIPT_DIR / "Figure_1.png"
OUT_PDF = SCRIPT_DIR / "Figure_1.pdf"

# Set to e.g. 1.10 to increase all text by 10%.
FONT_SCALE = 1.35
FONT_MAIN = 12 * FONT_SCALE
FONT_SMALL = 10 * FONT_SCALE
FONT_LABEL = 13 * FONT_SCALE
FONT_TITLE = 16 * FONT_SCALE

PATH_LW = 2.3
BEAM_LW = 2.5

COLOR_PUMP = "tab:purple"
COLOR_A = "tab:red"
COLOR_B = "tab:blue"
COLOR_NEUTRAL = "0.25"
COLOR_PANEL = "0.97"


# =============================================================================
# DRAWING HELPERS
# =============================================================================

def add_arrow(
    ax,
    start,
    end,
    color=COLOR_NEUTRAL,
    lw=PATH_LW,
    mutation_scale=14,
    zorder=3,
):
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


def add_spdc_crystal(ax, center, width=0.42, height=0.9):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width,
            height,
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


def add_double_slit(
    ax,
    center,
    width=0.42,
    height=1.0,
    slit_width=0.07,
    gap=0.08,
):
    x, y = center
    ax.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width,
            height,
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
                slit_width,
                slit_h,
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
            w,
            h,
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
            body_w,
            body_h,
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
            0.12 * scale,
            0.40 * scale,
            facecolor="0.88",
            edgecolor="0.15",
            linewidth=1.1,
            zorder=7,
        )
    )
    ax.add_patch(
        Rectangle(
            (x - 0.12 * scale, y + body_h / 2 - 0.02 * scale),
            0.24 * scale,
            0.10 * scale,
            facecolor="0.18",
            edgecolor="0.1",
            linewidth=1.0,
            zorder=6,
        )
    )


def add_correlation_box(ax, center, width=1.85, height=0.72):
    x, y = center
    x = x + 0.6
    ax.add_patch(
        FancyBboxPatch(
            (x - width / 2, y - height / 2),
            width,
            height,
            boxstyle="round,pad=0.03,rounding_size=0.08",
            facecolor="0.98",
            edgecolor=COLOR_PUMP,
            linewidth=1.7,
            zorder=5,
        )
    )
    ax.text(
        x,
        y + 0.08,
        "Coincidence",
        ha="center",
        va="center",
        fontsize=FONT_LABEL,
        weight="bold",
        color=COLOR_PUMP,
        zorder=6,
    )
    ax.text(
        x,
        y - 0.14,
        "correlation",
        ha="center",
        va="center",
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
    codes = [
        MplPath.MOVETO,
        MplPath.CURVE4,
        MplPath.CURVE4,
        MplPath.CURVE4,
    ]

    ax.add_patch(
        PathPatch(
            MplPath(vertices, codes),
            facecolor="none",
            edgecolor=color,
            linewidth=lw,
            zorder=3,
        )
    )


def add_plot_panel(ax, xywh, title, border_color, mode):
    x, y, w, h = xywh

    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=COLOR_PANEL,
            edgecolor=border_color,
            linewidth=1.35,
            zorder=2,
        )
    )
    ax.text(
        x + w / 2,
        y + h - 0.13,
        title,
        ha="center",
        va="top",
        fontsize=FONT_SMALL + 1 * FONT_SCALE,
        color=border_color,
        weight="bold",
    )

    px0, px1 = x + 0.20 * w, x + 0.91 * w
    py0, py1 = y + 0.30 * h, y + 0.70 * h

    ax.plot([px0, px1], [py0, py0], color="0.15", lw=1.0, zorder=3)
    ax.plot([px0, px0], [py0, py1], color="0.15", lw=1.0, zorder=3)

    if mode == "fixed":
        rng = np.random.default_rng(11)
        t = np.linspace(0.04, 0.98, 40)
        clicks = rng.integers(0, 2, size=t.size)
        xs = px0 + t * (px1 - px0)
        ys = py0 + clicks * 0.22 * h
        ax.scatter(xs, ys, s=12, color=COLOR_A, zorder=4)

        subtitle = "Clicks alone — no image"
        ax.text(px1, py0 - 0.04 * h, "time", ha="right", va="top", fontsize=FONT_SMALL)
        ax.text(px0 - 0.02 * w, py1, "click", ha="right", va="top", fontsize=FONT_SMALL)

    elif mode == "camera":
        rng = np.random.default_rng(13)
        n = 420
        xs = rng.uniform(px0, px1, n)
        ys = rng.uniform(py0 + 0.02 * h, py1 - 0.02 * h, n)
        ax.scatter(xs, ys, s=3.0, color=COLOR_B, alpha=0.60, zorder=4)

        subtitle = "Camera alone — no interference pattern"
        ax.text(px1, py0 - 0.04 * h, "time", ha="right", va="top", fontsize=FONT_SMALL)
        ax.text(px0 - 0.02 * w, py1, "position", ha="right", va="top", fontsize=FONT_SMALL)

    elif mode == "coincidence":
        xx = np.linspace(-4.2, 4.2, 600)
        envelope = np.sinc(xx / 4.0) ** 2
        fringes = 0.5 * (1 + np.cos(2 * np.pi * xx / 1.35))
        yy = envelope * fringes
        yy /= yy.max()

        xs = px0 + (xx - xx.min()) / (xx.max() - xx.min()) * (px1 - px0)
        ys = py0 + yy * (py1 - py0)
        ax.plot(xs, ys, color=COLOR_PUMP, lw=2.0, zorder=4)

        subtitle = "Interference appears in coincidences"
        ax.text(px1, py0 - 0.04 * h, "position", ha="right", va="top", fontsize=FONT_SMALL)
        ax.text(px0 - 0.02 * w, py1, "counts", ha="right", va="top", fontsize=FONT_SMALL)

    else:
        raise ValueError(f"Unknown mode: {mode}")

    ax.text(
        x + w / 2,
        y + 0.07,
        subtitle,
        ha="center",
        va="bottom",
        fontsize=FONT_SMALL,
        color="0.2",
    )


# =============================================================================
# FIGURE
# =============================================================================

def make_figure():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8.2)
    ax.axis("off")

    y_source = 5.75
    crystal = (3.1, y_source)

    # Pump and SPDC crystal
    add_arrow(
        ax,
        (0.55, y_source),
        (1.45, y_source),
        color=COLOR_PUMP,
        lw=3.2,
        mutation_scale=16,
    )
    ax.text(
        0.52,
        y_source + 0.32,
        "UV laser",
        fontsize=FONT_LABEL,
        color=COLOR_PUMP,
        ha="left",
    )
    add_beam(ax, (1.45, y_source), (3.0, y_source), COLOR_PUMP, lw=3.0, alpha=0.6)
    add_spdc_crystal(ax, crystal)
    ax.text(
        crystal[0],
        crystal[1] + 0.70,
        "SPDC crystal",
        ha="center",
        fontsize=FONT_LABEL,
    )

    # Photon A: double slit -> fixed detector
    slit = (8.16, 6.45)
    fixed = (10.6, 6.65)

    add_beam(ax, crystal, (10.15, 6.65), COLOR_A)
    add_double_slit(ax, slit)
    add_fixed_detector(ax, fixed)

    ax.text(
        4.45,
        6.43,
        "Photon A",
        color=COLOR_A,
        fontsize=FONT_LABEL,
        weight="bold",
    )
    ax.text(
        slit[0],
        slit[1] + 0.70,
        "double slit",
        ha="center",
        fontsize=FONT_LABEL,
    )
    ax.text(
        fixed[0] + 0.08,
        fixed[1] - 0.72,
        "fixed detector\n(no spatial resolution)",
        ha="center",
        va="top",
        fontsize=FONT_SMALL + 1 * FONT_SCALE,
    )

    # Photon B: directly to the camera
    camera = (10.65, 4.80)

    add_beam(ax, crystal, (10.10, 4.85), COLOR_B)
    add_camera(ax, camera)

    ax.text(
        4.25,
        4.88,
        "Photon B",
        color=COLOR_B,
        fontsize=FONT_LABEL,
        weight="bold",
    )
    ax.text(
        camera[0],
        camera[1] - 0.62,
        "camera\n(position-sensitive)",
        ha="center",
        va="top",
        fontsize=FONT_SMALL + 1 * FONT_SCALE,
    )

    # Coincidence electronics
    corr = (12.35, 5.65)
    add_correlation_box(ax, corr)
    add_curved_wire(ax, (10.72, 6.72), (11.98, 5.86))
    add_curved_wire(ax, (11.02, 4.82), (11.98, 5.37))

    # Lower explanatory panels
    add_plot_panel(ax, (0.55, 0.55, 3.95, 1.85), "fixed detector", COLOR_A, "fixed")
    add_plot_panel(ax, (5.05, 0.55, 3.95, 1.85), "Camera", COLOR_B, "camera")
    add_plot_panel(
        ax,
        (9.55, 0.55, 3.95, 1.85),
        "Coincidences",
        COLOR_PUMP,
        "coincidence",
    )

    ax.text(
        7.1,
        3.22,
        "Neither detector contains the interference pattern on its own",
        ha="center",
        va="center",
        fontsize=FONT_LABEL*1.2,
        color="0.22",
        weight="bold",
    )
    ax.text(
        11.1,
        0.12,
        "The pattern emerges in the correlation",
        ha="center",
        va="bottom",
        fontsize=FONT_LABEL,
        color=COLOR_PUMP,
        weight="bold",
    )

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
