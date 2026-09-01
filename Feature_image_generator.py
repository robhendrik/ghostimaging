"""
2D double-slit interference pattern with Gaussian illumination.

The field at the slit plane is:
    Gaussian amplitude (flat phase) × double-slit aperture

It is propagated to an observation plane with the Fresnel transfer function.

Dependencies:
    numpy
    matplotlib
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import os
os.chdir("GhostImaging")
print(os.getcwd())

# ============================================================
# SETTINGS
# ============================================================

# Optical parameters
WAVELENGTH = 702.2e-9           # m
PROPAGATION_DISTANCE = 1.50     # m, slits -> observation plane

# Double slit
SLIT_WIDTH = 0.15e-3            # m
SLIT_SEPARATION = 0.47e-3       # m, centre-to-centre
SLIT_LENGTH = 2.0e-3            # m

# Gaussian illumination
# Defined as the full 1/e^2 INTENSITY diameter.
GAUSSIAN_DIAMETER = 2.0e-3      # m
BEAM_CENTER_X = 0.0             # m
BEAM_CENTER_Y = 0.0             # m

# Numerical grid
GRID_SIZE = 2048                # pixels per dimension
WINDOW_SIZE = 20e-3             # m, physical width/height of simulated plane

# Display
DISPLAY_HALF_WIDTH_X = 8.0e-3   # m
DISPLAY_HALF_WIDTH_Y = 4.0e-3   # m
INTENSITY_GAMMA = 0.55          # <1 brightens weak fringes; 1 = linear
SHOW_AXES = False

# Output
OUTPUT_PNG = Path("Feature_image.png")
DPI = 220


# ============================================================
# HELPERS
# ============================================================

def blue_white_cmap():
    """Black -> blue -> pale blue -> white."""
    return LinearSegmentedColormap.from_list(
        "blue_white",
        [
            (0.00, "#000000"),
            (0.12, "#001229"),
            (0.38, "#004b9b"),
            (0.68, "#55bfff"),
            (1.00, "#ffffff"),
        ],
    )


def make_input_field(x, y):
    """Gaussian field with flat phase, clipped by two rectangular slits."""
    X, Y = np.meshgrid(x, y, indexing="xy")

    # If I(r) = exp(-2 r^2 / w^2), then 2w is the 1/e^2 intensity diameter.
    w = GAUSSIAN_DIAMETER / 2.0
    gaussian_amplitude = np.exp(
        -((X - BEAM_CENTER_X) ** 2 + (Y - BEAM_CENTER_Y) ** 2) / w**2
    )

    left_slit = (
        (np.abs(X + SLIT_SEPARATION / 2) <= SLIT_WIDTH / 2)
        & (np.abs(Y) <= SLIT_LENGTH / 2)
    )
    right_slit = (
        (np.abs(X - SLIT_SEPARATION / 2) <= SLIT_WIDTH / 2)
        & (np.abs(Y) <= SLIT_LENGTH / 2)
    )

    aperture = (left_slit | right_slit).astype(float)

    # Flat phase means the field is real and positive at the slit plane.
    return gaussian_amplitude * aperture


def fresnel_propagate(field, dx, wavelength, z):
    """
    Fresnel propagation using the transfer-function method.

    Global phase factors are omitted because they do not affect intensity.
    """
    ny, nx = field.shape
    fx = np.fft.fftfreq(nx, d=dx)
    fy = np.fft.fftfreq(ny, d=dx)
    FX, FY = np.meshgrid(fx, fy, indexing="xy")

    H = np.exp(-1j * np.pi * wavelength * z * (FX**2 + FY**2))

    field_f = np.fft.fft2(field)
    propagated = np.fft.ifft2(field_f * H)
    return propagated


def main():
    dx = WINDOW_SIZE / GRID_SIZE
    x = (np.arange(GRID_SIZE) - GRID_SIZE / 2) * dx
    y = (np.arange(GRID_SIZE) - GRID_SIZE / 2) * dx

    field0 = make_input_field(x, y)
    field_z = fresnel_propagate(
        field0, dx, WAVELENGTH, PROPAGATION_DISTANCE
    )

    intensity = np.abs(field_z) ** 2
    intensity /= intensity.max()

    # Gamma is only for display; the underlying intensity remains linear.
    display_intensity = intensity ** INTENSITY_GAMMA

    extent_mm = [
        x[0] * 1e3,
        x[-1] * 1e3,
        y[0] * 1e3,
        y[-1] * 1e3,
    ]

    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor="black")
    ax.set_facecolor("black")

    ax.imshow(
        display_intensity,
        extent=extent_mm,
        origin="lower",
        cmap=blue_white_cmap(),
        vmin=0,
        vmax=1,
        interpolation="bilinear",
        aspect="equal",
    )

    ax.set_xlim(-DISPLAY_HALF_WIDTH_X * 1e3, DISPLAY_HALF_WIDTH_X * 1e3)
    ax.set_ylim(-DISPLAY_HALF_WIDTH_Y * 1e3, DISPLAY_HALF_WIDTH_Y * 1e3)

    if SHOW_AXES:
        ax.set_xlabel("x on observation plane (mm)", color="white")
        ax.set_ylabel("y on observation plane (mm)", color="white")
        ax.tick_params(colors="white")
        for spine in ax.spines.values():
            spine.set_color("white")
    else:
        ax.set_axis_off()

    fig.tight_layout(pad=0)
    fig.savefig(
        OUTPUT_PNG,
        dpi=DPI,
        facecolor=fig.get_facecolor(),
        bbox_inches="tight",
        pad_inches=0,
    )
    plt.close(fig)


if __name__ == "__main__":
    main()
