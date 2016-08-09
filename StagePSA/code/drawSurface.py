"""This is a module to draw B-Spline and NURBS Surface. The main implementation lies in
``drawWithBSpline`` and ``drawWithNURBS``.

Example:
::

    knot1 = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]
    knot2 = [0, 0, 1, 1]
    a = np.sqrt(1.0/2)
    B = np.array([[[1, 0], [2, 0]],
                  [[1, 1], [2, 2]],
                  [[0, 1], [0, 2]],
                  [[-1, 1], [-2, 2]],
                  [[-1, 0], [-2, 0]],
                  [[-1, -1], [-2, -2]],
                  [[0, -1], [0, -2]],
                  [[1, -1], [2, -2]],
                  [[1, 0], [2, 0]]])
    w = [[1, 1],
         [a, a],
         [1, 1],
         [a, a],
         [1, 1],
         [a, a],
         [1, 1],
         [a, a],
         [1, 1]]
    #drawWithBSpline(knot1, knot2, B, p1=2, p2=1, nPoint1=49, nPoint2=9)
    drawWithNURBS(knot1, knot2, B, np.array(w), p1=2, p2=1, nPoint1=9, nPoint2=9)
    plt.show()

"""


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.lines as lines
from NURBS import BSplineArray as NA

def drawArray2D(arrBig, nx1, nx2, knot1, knot2, withCurve=False):
    """Procedure to plot a 2D array.

    Note:
        This was used mainly for debugging. At user-level, please use ``drawWithBSpline`` and ``drawWithNURBS``.

    Args:
        arrBig (2D point array): array of size (nx1, nx2) that is a discretisation of parametric space.
        nx1 (int): number of points used in discretisation of the first dimension.
        nx2 (int): number of points used in discretisation of the second dimension.
        knot1 (point array): knot vector of the first dimension.
        knot2 (point array): knot vector of the second dimension.
        withCurve (bool): if ``True`` than plot parametric curves (default=False).

    """
    knotI1 = map(int,np.array(knot1)*(nx1-1)*1.0/knot1[-1])[1:]
    knotI2 = map(int,np.array(knot2)*(nx2-1)*1.0/knot2[-1])[1:]
    if arrBig.shape[0:2] != (nx1, nx2):
        print 'Dimensions not match'
        return
    patches = []
    # Add Surface
    for i in range(nx1 - 1):
        for j in range(nx2 - 1):
            polygontmp = Polygon([ arrBig[i,j], arrBig[i+1,j], arrBig[i+1,j+1], arrBig[i,j+1]], True)
            patches.append(polygontmp)
    p = PatchCollection(patches, cmap = matplotlib.cm.jet, alpha = 0.4)
    fig, ax = plt.subplots()
    # Add Curves
    if withCurve:
        for i in knotI1:
            for j in range(nx2 - 1):
                plt.plot([arrBig[i,j][0], arrBig[i,j+1][0]], [arrBig[i,j][1], arrBig[i,j+1][1]], c = 'red', linewidth=2)
        for j in knotI2:
            for i in range(nx1 - 1):
                plt.plot([arrBig[i,j][0], arrBig[i+1,j][0]], [arrBig[i,j][1], arrBig[i+1,j][1]], c = 'red', linewidth=2)
    ax.add_collection(p)
    return

def drawWithBSpline(knot1, knot2, arrayB, p1=2, p2=2, nPoint1=25, nPoint2=25, withCurve=False):
    """Procedure to plot a B-Spline Surface.

    Args:
        knot1 (point array): knot vector of the first dimension.
        knot2 (point array): knot vector of the second dimension.
        arrayB (2D point array): array of base points.
        p1 (int): horizontal polynomial degree(default=2).
        p2 (int): vertical polynomial degree(default=2).
        nPoint1 (int): number of points used in discretisation of the horizonal dimension (default=25).
        nPoint2 (int): number of points used in discretisation of the vertical dimension(default=25).
        withCurve (bool): if ``True`` than plot parametric curves (default=False).

    """
    knotVector1 = np.append(-1, knot1)
    knotVector2 = np.append(-1, knot2)
    arrB = np.array(arrayB)
    knotVector1 = map(float, knotVector1)
    knotVector2 = map(float, knotVector2)

    nx1 = nPoint1
    nx2 = nPoint2
    xi1 = np.linspace(knot1[0], knot1[-1], nx1)
    xi2 = np.linspace(knot2[0], knot2[-1], nx2)

    arrN1 = np.array([NA(knotVector1, p1, k)[1:] for k in xi1])
    arrN2 = np.array([NA(knotVector2, p2, k)[1:] for k in xi2])
    arrS = []

    arrS = np.array([[sum(map(sum,
            [[arrN1[x1, i]*arrN2[x2, j]*arrB[i, j] for i in range(len(arrN1[0]))] for j in range(len(arrN2[0]))]))
            for x2 in range(nx2)] for x1 in range(nx1)])

    x1, x2 = np.meshgrid(xi1, xi2)
    drawArray2D(arrS, nx1, nx2, knotVector1, knotVector2,withCurve)

    #scatter base points
    #flatArrB = arrB.reshape((arrB.shape[0]*arrB.shape[1], 2))
    #plt.scatter(flatArrB[:, 0], flatArrB[:, 1], s=40, c='green')

def drawWithNURBS(knot1, knot2, arrayB, w, p1=2, p2=2, nPoint1=15, nPoint2=15, withCurve=False):
    """Procedure to plot a NURBS Surface.

    Args:
        knot1 (point array): knot vector of the first dimension.
        knot2 (point array): knot vector of the second dimension.
        arrayB (2D point array): array of base points.
        w (2D float array): weight array.
        p1 (int): horizontal polynomial degree(default=2).
        p2 (int): vertical polynomial degree(default=2).
        nPoint1 (int): number of points used in discretisation of the horizonal dimension (default=25).
        nPoint2 (int): number of points used in discretisation of the vertical dimension(default=25).
        withCurve (bool): if ``True`` than plot parametric curves (default=False).

    """

    knotVector1 = np.append(-1,knot1)
    knotVector2 = np.append(-1, knot2)
    arrB = np.array(arrayB)
    knotVector1 = map(float, knotVector1)
    knotVector2 = map(float, knotVector2)

    nx1 = nPoint1
    nx2 = nPoint2
    xi1 = np.linspace(knot1[0], knot1[-1], nx1)
    xi2 = np.linspace(knot2[0], knot2[-1], nx2)

    arrN1 = np.array([NA(knotVector1, p1, k)[1:] for k in xi1])
    arrN2 = np.array([NA(knotVector2, p2, k)[1:] for k in xi2])
    arrS = []

    for x1 in range(nx1):
        row = []
        for x2 in range(nx2):
            Rij = np.array([w[i,j]*arrN1[x1, i]*arrN2[x2, j] for i in range(len(arrN1[0])) for j in range(len(arrN2[0]))])
            Rij = Rij/sum(Rij)
            row.append(np.dot(Rij,[arrB[i, j] for i in range(len(arrN1[0])) for j in range(len(arrN2[0]))]))
        arrS.append(row)
    arrS = np.array(arrS)

    x1, x2 = np.meshgrid(xi1, xi2)
    drawArray2D(arrS, nx1, nx2, knotVector1, knotVector2,withCurve)

    flatArrB = arrB.reshape((arrB.shape[0]*arrB.shape[1], 2))
    plt.scatter(flatArrB[:, 0], flatArrB[:, 1], s=40, c='green')
    #plt.show()


def exampleBSpline():
    knot1 = [0, 0, 0, 0.5, 1, 1, 1]
    knot2 = [0, 0, 0, 1, 1, 1]
    B = np.array([[[0, 0], [-1, 0], [-2, 0]],
                  [[0, 1], [-1, 2], [-2, 2]],
                  [[1, 1.5], [1, 4], [1, 5]],
                  [[3, 1.5], [3, 4], [3, 5]]])
    drawWithBSpline(knot1, knot2, B, nPoint1=19, nPoint2=19)
    plt.show()


def exampleNURBS():
    knot1 = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]
    knot2 = [0, 0, 1, 1]
    a = np.sqrt(1.0/2)
    B = np.array([[[1, 0], [2, 0]],
                  [[1, 1], [2, 2]],
                  [[0, 1], [0, 2]],
                  [[-1, 1], [-2, 2]],
                  [[-1, 0], [-2, 0]],
                  [[-1, -1], [-2, -2]],
                  [[0, -1], [0, -2]],
                  [[1, -1], [2, -2]],
                  [[1, 0], [2, 0]]])
    w = [[1, 1],
         [a, a],
         [1, 1],
         [a, a],
         [1, 1],
         [a, a],
         [1, 1],
         [a, a],
         [1, 1]]
    #drawWithBSpline(knot1, knot2, B, p1=2, p2=1, nPoint1=49, nPoint2=9)
    drawWithNURBS(knot1, knot2, B, np.array(w), p1=2, p2=1, nPoint1=9, nPoint2=9)
    plt.show()

def main():
    #exampleBSpline()
    exampleNURBS()

if __name__ == "__main__":
    main()
