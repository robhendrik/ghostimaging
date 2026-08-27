#!/usr/bin/env python3
"""
Klyshko advanced-wave picture for a ghost double-slit experiment.

Top:
    SPDC ghost-imaging setup.
    UV laser -> SPDC crystal.
    Photon A -> double slit -> bucket detector.
    Photon B -> camera.
    Bucket and camera feed a coincidence-correlation unit.

Bottom:
    Klyshko equivalent.
    The bucket detector is replaced by a classical light source.
    The SPDC crystal is replaced by a mirror.
    Light propagates from the former bucket position, through the double slit,
    to the mirror, then onward to the camera.

The lower panel deliberately contains:
    - no pump laser
    - no Photon A / Photon B labels
    - no coincidence electronics

Outputs:
    klyshko_ghost_imaging_schematic.png
    klyshko_ghost_imaging_schematic.pdf
"""

from __future__ import annotations

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Ellipse, FancyArrowPatch
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

FIGSIZE = (14, 8.5)
DPI = 220
SCRIPT_DIR = Path(__file__).resolve().parent
OUT_PNG = SCRIPT_DIR / "klyshko_ghost_imaging_schematic.png"
OUT_PDF = SCRIPT_DIR / "klyshko_ghost_imaging_schematic.pdf"

FONT_SMALL = 10
FONT_LABEL = 12
FONT_PANEL = 15
COLOR_PUMP = "tab:purple"
COLOR_A = "tab:red"
COLOR_B = "tab:blue"
COLOR_K = "0.20"
COLOR_NEUTRAL = "0.22"
PATH_LW = 2.4


def add_beam(ax, start, end, color, lw=PATH_LW, alpha=0.95, zorder=2):
    ax.plot([start[0], end[0]], [start[1], end[1]], color=color,
            linewidth=lw, alpha=alpha, solid_capstyle="round", zorder=zorder)


def add_arrow(ax, start, end, color=COLOR_NEUTRAL, lw=1.8,
              mutation_scale=14, zorder=3):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>",
                                 mutation_scale=mutation_scale,
                                 linewidth=lw, color=color,
                                 shrinkA=0, shrinkB=0, zorder=zorder))


def add_spdc_crystal(ax, center, width=0.42, height=0.88):
    x, y = center
    ax.add_patch(Rectangle((x-width/2, y-height/2), width, height,
                           linewidth=1.4, edgecolor=COLOR_PUMP,
                           facecolor="0.93", zorder=6))
    ax.plot([x-width/2, x, x+width/2],
            [y+height/2, y+height*0.67, y+height/2],
            color=COLOR_PUMP, linewidth=1.0, zorder=7)


def add_double_slit(ax, center, width=0.42, height=0.98,
                    slit_width=0.07, gap=0.08):
    x, y = center
    ax.add_patch(Rectangle((x-width/2, y-height/2), width, height,
                           facecolor="0.08", edgecolor="0.08", zorder=7))
    slit_h = height * 0.72
    slit_y = y - slit_h/2
    for sx in (x-gap/2-slit_width, x+gap/2):
        ax.add_patch(Rectangle((sx, slit_y), slit_width, slit_h,
                               facecolor="white", edgecolor="white", zorder=8))


def add_bucket_detector(ax, center, scale=1.0):
    x, y = center
    w, h = 0.52*scale, 0.55*scale
    ax.add_patch(FancyBboxPatch((x-w/2, y-h/2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                facecolor="0.78", edgecolor="0.15",
                                linewidth=1.3, zorder=6))
    ax.add_patch(Ellipse((x-w/2, y), width=0.16*scale, height=0.42*scale,
                         facecolor="0.55", edgecolor="0.15",
                         linewidth=1.1, zorder=7))


def add_camera(ax, center, scale=1.0):
    x, y = center
    body_w, body_h = 0.74*scale, 0.48*scale
    ax.add_patch(FancyBboxPatch((x-body_w/2, y-body_h/2), body_w, body_h,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                facecolor="0.25", edgecolor="0.1",
                                linewidth=1.3, zorder=6))
    ax.add_patch(Rectangle((x-body_w/2-0.10*scale, y-0.20*scale),
                           0.12*scale, 0.40*scale,
                           facecolor="0.88", edgecolor="0.15",
                           linewidth=1.1, zorder=7))
    ax.add_patch(Rectangle((x-0.12*scale, y+body_h/2-0.02*scale),
                           0.24*scale, 0.10*scale,
                           facecolor="0.18", edgecolor="0.1",
                           linewidth=1.0, zorder=6))


def add_correlation_box(ax, xy, width=1.55, height=0.72):
    x, y = xy
    ax.add_patch(FancyBboxPatch((x-width/2, y-height/2), width, height,
                                boxstyle="round,pad=0.03,rounding_size=0.08",
                                facecolor="0.98", edgecolor=COLOR_PUMP,
                                linewidth=1.7, zorder=5))
    ax.text(x, y+0.08, "Coincidence", ha="center", va="center",
            fontsize=FONT_LABEL, weight="bold", color=COLOR_PUMP, zorder=6)
    ax.text(x, y-0.14, "correlation", ha="center", va="center",
            fontsize=FONT_LABEL, color=COLOR_PUMP, zorder=6)


def add_curved_wire(ax, start, end, color="0.15", lw=1.7, bend=0.35):
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    verts = [(x0, y0), (x0+bend*dx, y0), (x1-bend*dx, y1), (x1, y1)]
    codes = [MplPath.MOVETO, MplPath.CURVE4, MplPath.CURVE4, MplPath.CURVE4]
    ax.add_patch(PathPatch(MplPath(verts, codes), facecolor="none",
                           edgecolor=color, linewidth=lw, zorder=3))


def add_mirror(ax, center, length=0.82, angle_deg=-45):
    x, y = center
    theta = np.deg2rad(angle_deg)
    dx = (length/2) * np.cos(theta)
    dy = (length/2) * np.sin(theta)
    ax.plot([x-dx, x+dx], [y-dy, y+dy], color="0.35",
            linewidth=6.0, solid_capstyle="round", zorder=7)
    ax.plot([x-dx, x+dx], [y-dy, y+dy], color="0.85",
            linewidth=2.2, solid_capstyle="round", zorder=8)


def add_simple_laser(ax, center, direction="left", scale=1.0):
    x, y = center
    body_w, body_h = 0.58*scale, 0.34*scale
    ax.add_patch(FancyBboxPatch((x-body_w/2, y-body_h/2), body_w, body_h,
                                boxstyle="round,pad=0.02,rounding_size=0.04",
                                facecolor="0.82", edgecolor="0.15",
                                linewidth=1.2, zorder=6))
    aperture_x = x-body_w/2 if direction == "left" else x+body_w/2
    ax.add_patch(Ellipse((aperture_x, y), width=0.12*scale, height=0.25*scale,
                         facecolor="0.50", edgecolor="0.15",
                         linewidth=1.0, zorder=7))


def draw_quantum_panel(ax):
    y_source = 6.45
    crystal = (3.10, y_source)
    slit = (8.10, 6.95)
    bucket = (10.58, 6.95)
    camera = (10.62, 5.55)
    corr = (12.28, 6.25)

    ax.text(0.55, 7.65, "a   Two-photon ghost experiment",
            fontsize=FONT_PANEL, weight="bold", color="0.15")

    add_arrow(ax, (0.55, y_source), (1.45, y_source),
              color=COLOR_PUMP, lw=3.0, mutation_scale=15)
    add_beam(ax, (1.45, y_source), (2.88, y_source),
             COLOR_PUMP, lw=3.0, alpha=0.55)
    ax.text(0.55, y_source+0.30, "UV laser",
            color=COLOR_PUMP, fontsize=FONT_LABEL)

    add_spdc_crystal(ax, crystal)
    ax.text(crystal[0], crystal[1]+0.66, "SPDC crystal",
            ha="center", fontsize=FONT_LABEL)

    add_beam(ax, crystal, (10.15, 6.95), COLOR_A)
    add_double_slit(ax, slit)
    add_bucket_detector(ax, bucket)
    ax.text(4.45, 7.25, "Photon A", color=COLOR_A,
            fontsize=FONT_LABEL, weight="bold")
    ax.text(slit[0], slit[1]+0.63, "double slit",
            ha="center", fontsize=FONT_LABEL)
    ax.text(bucket[0], bucket[1]-0.72,
            "bucket detector\n(no spatial resolution)",
            ha="center", va="top", fontsize=FONT_SMALL+1)

    add_beam(ax, crystal, (10.08, 5.58), COLOR_B)
    add_camera(ax, camera)
    ax.text(4.28, 5.68, "Photon B", color=COLOR_B,
            fontsize=FONT_LABEL, weight="bold")
    ax.text(camera[0], camera[1]-0.58,
            "camera\n(position-sensitive)",
            ha="center", va="top", fontsize=FONT_SMALL+1)

    add_correlation_box(ax, corr)
    add_curved_wire(ax, (10.85, 7.00), (11.50, 6.43))
    add_curved_wire(ax, (11.00, 5.56), (11.50, 6.06))


def draw_klyshko_panel(ax):
    mirror = (3.10, 2.50)
    slit = (8.10, 2.95)
    source = (10.58, 3.10)
    camera = (10.62, 1.90)

    ax.text(0.55, 3.78, "b   Klyshko equivalent",
            fontsize=FONT_PANEL, weight="bold", color="0.15")

    add_simple_laser(ax, source, direction="left", scale=1.05)
    ax.text(source[0], source[1]+0.46, "light source",
            ha="center", fontsize=FONT_LABEL)

    add_double_slit(ax, slit)
    ax.text(slit[0], slit[1]+0.63, "double slit",
            ha="center", fontsize=FONT_LABEL)

    add_mirror(ax, mirror, length=0.90, angle_deg=90)
    ax.text(mirror[0]-0.02, mirror[1]+0.73, "mirror",
            ha="center", fontsize=FONT_LABEL)

    add_camera(ax, camera)
    ax.text(camera[0], camera[1]-0.58, "camera",
            ha="center", va="top", fontsize=FONT_SMALL+1)

    # Advanced-wave path: former bucket position -> double slit -> mirror -> camera
    add_beam(ax, (10.25, 3.10), mirror, COLOR_K, lw=2.6)
    add_beam(ax, mirror, (10.08, 1.93), COLOR_K, lw=2.6)

    # Arrowheads show the propagation direction in the unfolded picture.
    add_arrow(ax, (10.25, 3.10), mirror,
              color=COLOR_K, lw=1.7, mutation_scale=12)
    add_arrow(ax, mirror, (10.08, 1.93),
              color=COLOR_K, lw=1.7, mutation_scale=12)


    ax.text(6.55, 1.20,
            "The two-photon geometry unfolds into one ordinary optical path",
            ha="center", fontsize=FONT_LABEL, color="0.30", style="italic")


def make_figure():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    ax.set_xlim(0, 14)
    ax.set_ylim(0.8, 8.1)
    ax.axis("off")

    draw_quantum_panel(ax)
    draw_klyshko_panel(ax)

    ax.plot([0.55, 13.45], [4.45, 4.45], color="0.82", linewidth=1.0, zorder=1)

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
