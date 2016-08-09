"""This is a module to draw base functions of isogeometric analysis. It uses the functions ``BSpline`` and ``BSplineArray`` from the NURBS Module.

This module was used mainly for debugging purposes.

Example:
::

    #Taken from __main__, so you can just call ``python drawNURBS.py`` instead.
    drawb([0, 0, 0, 1, 1, 1])

Please see ``main()`` for other examples.
"""


import numpy as np
import matplotlib.pyplot as plt
from NURBS import BSpline as N
from NURBS import BSplineArray as NA

# ------  default ------
# 50 steps for x
#
def draw(knot, p=2,nPoint=200):
    """Draw base functions from knot vector and polynomial degree.

    Args:
        knot (float array): knot vector.
        p (int): polynomial degree.
        nPoint (int): number of points for discretization (default=200).

    Note:
        This is a depricated methode, please use ``drawb`` instead.


    """
    knotVector = [-1] + knot
    knotVector = map(float, knotVector)

    x = np.linspace(knot[0], knot[-1], nPoint)
    axes = plt.gca()
    iMax = len(knotVector) - 1 - p

    axes.set_ylim([0, 1.5])
    axes.set_xlim([-0.5 + knot[0], 0.5 + knot[-1]])
    for i in range(1, iMax):
        plt.plot(x, [N(knotVector, i, p, k) for k in x])
    plt.show()

def drawb(knot, p=2, nPoint=200):
    """Draw base functions from knot vector and polynomial degree.

    Args:
        knot (float array): knot vector.
        p (int): polynomial degree.
        nPoint (int): number of points for discretization (default=200).

    """
    knotVector = [-1] + knot
    knotVector = map(float, knotVector)

    x = np.linspace(knot[0], knot[-1], nPoint)
    axes = plt.gca()

    axes.set_ylim([0, 1.5])
    axes.set_xlim([-0.5 + knot[0], 0.5 + knot[-1]])
    y = np.array([NA(knotVector, p, k) for k in x])
    for i in range(1,len(y[0])):
            plt.plot(x, y[:, i])
    plt.show()

def main():
#    drawb([0, 0, 0, 0, 0, 1.0/3, 1.0/3, 1.0/3, 1.0/3, 2.0/3, 2.0/3, 2.0/3, 2.0/3, 1, 1, 1, 1, 1], 4)
#    drawb([0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5], 2)
    drawb([0, 0, 0, 1, 1, 1])

if __name__ == "__main__":
    main()
