"""This is my first approach to mesh a trimmed surface. The idea is that in
certain case (and quite frequent then), it is safe to assume that there is only
one trim, then one just need to construct a 2D NURBS surface that have the square
(boundary) and the trimming curve as its boundary.

See Also:
    `My Notebook <https://darknmt.github.io/StagePSA/wiki>`_ for more details

"""

import numpy as np
from NURBS_Class import BSpline
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.lines as lines
import matplotlib
from drawSurface import drawWithBSpline

###################################
#          Test goes here         #
###################################

def main():

    """This is a demonstration of my idea explained in the note above.

    Args:
        rec (B-Spline) : the boundary line of the parametric square.
        trimCurve (B-Spline) : the trimming curve.
        psing1 (point) : the chosen point on **trimCurve**
        psing2 (point) : the chosen point on **rec**
        tmp (B-Spline) : a line (or any B-Spline) connecting **psing1** and **psing2**

    """

    #draw square
    a = BSpline([0, 0, 0, 1, 1, 1], [[2, 2], [0, 2], [-2, 2]])
    b = BSpline([0, 0, 0, 1, 1, 1], [[2, -2], [2, 0], [2, 2]])
    c = BSpline([0, 0, 0, 1, 1, 1], [[-2, -2], [0, -2], [2, -2]])
    d = BSpline([0, 0, 0, 1, 1, 1], [[-2, 2], [-2, 0], [-2, -2]])
    rec = b+a+d+c
    #rec.drawCurve()

    #draw trimming curve
    psing1 = np.array([0.3, -0.7])
    psing2 = np.array([2, -2])
    a = BSpline([0, 0, 0, 1, 1, 1], [psing1, [1.3, -0.7], [1.3, 0.3]])
    b = BSpline([0, 0, 0, 1, 1, 1], [[1.3, 0.3], [1.3, 1.3], [0.3, 1.3]])
    c = BSpline([0, 0, 0, 1, 1, 1], [[0.3, 1.3], [-0.7, 1.3], [-0.7, 0.3]])
    d = BSpline([0, 0, 0, 1, 1, 1], [[-0.7, 0.3], [-0.7, -0.7], psing1])
    trimCurve = a+b+c+d
    #trimCurve.drawCurve()
    print "\nTrimming curve: \n" + str(trimCurve)
    print "\nRectangle: \n" + str(rec)

    tmp = BSpline([0,0,1,1], [psing1, psing2])
    #tmp.drawCurve()

    #Old approach
    #bigCurve = tmp + rec + tmp.reverse() + trimCurve.reverse()
    #bigCurve.drawCurve()
    #plt.xlim([-3,3])
    #plt.ylim([-3,3])

    bigB = np.concatenate(([rec.Base], [trimCurve.Base]))
    drawWithBSpline(tmp.knot, rec.knot, bigB,1, 2, 15, 41,withCurve=True)

    plt.xlim([-3,3])
    plt.ylim([-3,3])
    plt.show()

if __name__ == "__main__":
    main()
