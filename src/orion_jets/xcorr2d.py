"""
Two-dimensional cross correlation
"""

import numpy as np
from scipy import signal


def max_location_indices(arr: np.ndarray) -> tuple[int, ...]:
    """Return array indices of maximum value in `arr`

    This behaves like maxloc() in Fortran
    """
    return np.unravel_index(np.argmax(arr), arr.shape)


def measure_shift_integer(
    img_ref: np.ndarray, img_new: np.ndarray
) -> tuple[float, float]:
    """
    Measure (dy, dx) that best aligns img_new onto img_ref using 2D cross-correlation.

    Convention:
        img_new(y + dy, x + dx) ≈ img_ref(y, x)
    so positive dy, dx mean img_new must be shifted down/right to match img_ref.
    """

    assert len(img_ref.shape) == 2, "Images must be two-dimensional"
    assert img_ref.shape == img_new.shape, "Images mut be the same shape"

    # 2D cross-correlation: slide img_new over img_ref
    corr = signal.correlate2d(
        img_ref,
        img_new,
        mode="full",
        boundary="fill",
        fillvalue=0.0,
    )

    # Location of maximum correlation
    max_y, max_x = max_location_indice(corr)

    # Zero-lag position in 'full' correlation
    # For correlate2d(ref, new): zero lag is at (ref_shape - 1)
    y0 = img_new.shape[0] - 1
    x0 = img_new.shape[1] - 1

    # Lags (dy, dx)
    dy = max_y - y0
    dx = max_x - x0

    return float(dy), float(dx)


def xcorr_scipy(): ...
