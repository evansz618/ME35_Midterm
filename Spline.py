#!/usr/bin/env python3
# *_* coding: utf-8 *_*

from scipy.interpolate import CubicSpline
from scipy.interpolate import CubicHermiteSpline
from scipy.interpolate import PchipInterpolator
import matplotlib.pyplot as plt
import numpy as np
"""
Required Packages:
====================================================
pip3 install matplotlib  # Plotting!
pip3 install scipy       # spline interpolation
pip3 install numpy       # vector / matrix library

Also useful:
====================================================
pip3 install yapf        # autoformatting

License:  MIT
"""


def main():
    """
    Simple script to compare different types of spline interpolation.

    Constructs several types of interpolation splines through the same
    data set and plots them. This makes it simple to compare the pros
    and cons for each type of interpolator. The object returned by the
    interpolation solver code are fancy wrappers around vectors of 
    polynomial coefficients. You can read the docs for the interpolation
    library to figure out how to grab these coefficients and do interesting
    things with them. For example, you can manually joint two splines 
    together end to end, or evaluate the splines using your own code.

    See also:
    https://docs.scipy.org/doc/scipy/reference/interpolate.html#module-scipy.interpolate

    Notation:
      t = time (input)
      y = value (output)
    """

    # Arbitrary data to fit the spline through.
    # Try experimenting with changing these values or adding more.
    y_knots = np.array([-.16, -.14, -.16])

    # derivative (slope) at the knots, used only for cubic hermite.
    dy_knots = np.array([2, 0, 0])

    # Fit the spline through the "knot" points
    # Must be monotonically increasing, but not necessarily uniformly spaced
    t_knots = np.array([-0.0635, -0.04, 0.0635])

    # Plot the spline using the "evaluation" points
    t_eval = np.linspace(t_knots[0], t_knots[-1], 200)

    # Empty dictionary, we will add different types of interpolation
    # splines here. This can then be used later on by plotting code.
    y_traj = dict()

    # Here are two common boundary conditions used for cubic "spline" interplation.
    # Try experimenting with different boundary condition types (`bc_type`)
    # - Pro: smooth (continuous acceleration)
    # - Con: globally coupled, overshoot ("ringing"), requires sparse solve
    #y_traj["spline_natural"] = CubicSpline(t_knots, y_knots, bc_type='natural')
    #print(y_traj)
    #y_traj["spline_clamped"] = CubicSpline(t_knots, y_knots, bc_type='clamped')

    # Here I manually set zero velocity at the knots. Experiment with other choices
    # for the slopes and see how that affects the interpolation.
    # - Pro: really simple, exact control over shape, locally coupled
    # - Con: need to select good slopes, discontinuous acceleration
    y_traj["cubic_hermite"] = CubicHermiteSpline(t_knots, y_knots, dy_knots)
    
    points = []
    check_x = np.arange(-0.0635, 0.0635,0.0025)
    for i in range(len(check_x)):
        num = check_x[i]
        print(y_traj["cubic_hermite"](num))
        points.append(y_traj["cubic_hermite"](num))
    print(points)
    # Uses a fancy heuristic to compute the intermediate slopes, then uses the
    # interpolation under the hood to construct the spline.
    # - Pro: no overshoot, locally coupled, no need for interior slopes
    # - Con: discontinuous acceleration
    #y_traj["monotone_pchip"] = PchipInterpolator(t_knots, y_knots)

    # Give names to derivatives to make plotting code more readable.
    POS = 0
    VEL = 1
    ACC = 2

    # Set up the figure and axes
    fig, axes = plt.subplots(ncols=1, nrows=3, num=4, figsize=(9, 12))
    axes[POS].plot(t_knots, y_knots, 'o')

    # Plot each of the interpolation methods
    for name, spline in y_traj.items():

        axes[POS].scatter(t_eval, spline(t_eval, POS), label=name)

        axes[VEL].plot(t_knots, spline(t_knots, VEL), 'o', mfc='none')
        axes[VEL].plot(t_eval, spline(t_eval, VEL), label=name)

        axes[ACC].plot(t_knots, spline(t_knots, ACC), 'o', mfc='none')
        axes[ACC].plot(t_eval, spline(t_eval, ACC), label=name)

    # Clean up the plots a bit:
    for idx, label in enumerate(("position", "velocity", "acceleration")):
        axes[idx].legend()
        axes[idx].set(xlabel='time', ylabel=label)
        axes[idx].set_xlim(t_knots[0], t_knots[-1])

    plt.show()


if '__main__' == __name__:
    main()