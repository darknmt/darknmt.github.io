"""Implementation of NURBS/BSpline class
We overide the __add__ operator to join 2 NURBS/BSpline quickly by sing NURBS1 + NURBS2.
Our code is more adapted for second-order NURBS.

Examples:
    A square created by joining parallel lines.
    ::

        a = BSpline([0, 0, 0, 1, 1, 1], [[2, 2], [0, 2], [-2, 2]])
        b = BSpline([0, 0, 0, 1, 1, 1], [[2, -2], [2, 0], [2, 2]])
        c = BSpline([0, 0, 0, 1, 1, 1], [[-2, -2], [0, -2], [2, -2]])
        d = BSpline([0, 0, 0, 1, 1, 1], [[-2, 2], [-2, 0], [-2, -2]])
        rec = b+a+d+c
        rec.drawCurve()

    A curve created by joining 4 NURBS.
    ::

        a = BSpline([0, 0, 0, 1, 1, 1], [[0.3, -0.7], [1.3, -0.7], [1.3, 0.3]])
        b = BSpline([0, 0, 0, 1, 1, 1], [[1.3, 0.3], [1.3, 1.3], [0.3, 1.3]])
        c = BSpline([0, 0, 0, 1, 1, 1], [[0.3, 1.3], [-0.7, 1.3], [-0.7, 0.3]])
        d = BSpline([0, 0, 0, 1, 1, 1], [[-0.7, 0.3], [-0.7, -0.7], [0.3, -0.7]])
        trimCurve = a+b+c+d
        trimCurve.drawCurve()

Todo:
    * Add weight to have NURBS from BSpline
"""

import numpy as np
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
from NURBS import NURBSArray as RA


class BSpline(object):
#    knot =[]
#    Base = []
#    p = 2
    def __init__(self, dknot, dB, dp=2):
        self.knot = np.array(map(float,dknot))
        self.knot = self.knot/self.knot[-1]
        self.Base = np.array(dB)
        self.p = dp

    def drawCurve(self,nPoint=300, c='red', lw=1):
        """Drawing NURBS/BSpline using matplotlib

        Args:
            nPoint=300 (int) : number of discret points (default: 300)
            c='red' : color (default: 'red')
            lw=1 : line width (default = 1)

        Example:
        .. doctest::
            >>> a = BSpline([0, 0, 0, 1, 1, 1], [[0.3, -0.7], [1.3, -0.7], [1.3, 0.3]])
            >>> b = BSpline([0, 0, 0, 1, 1, 1], [[1.3, 0.3], [1.3, 1.3], [0.3, 1.3]])
            >>> c = BSpline([0, 0, 0, 1, 1, 1], [[0.3, 1.3], [-0.7, 1.3], [-0.7, 0.3]])
            >>> d = BSpline([0, 0, 0, 1, 1, 1], [[-0.7, 0.3], [-0.7, -0.7], [0.3, -0.7]])
            >>> trimCurve = a+b+c+d
            >>> trimCurve.drawCurve()

        """
        knotVector = np.append(-1,self.knot)
        knotVector = map(float, knotVector)
        xi = np.linspace(self.knot[0], self.knot[-1], nPoint)
        arrB = np.array(self.Base)
        arrN = np.array([NA(knotVector, self.p, k)[1:] for k in xi])
        data = np.dot(arrN, arrB)
        data = data[range(data.shape[0]),:]
        plt.plot(data[:,0], data[:,1], color=c, linewidth=lw)
        #plt.scatter(arrB[:, 0], arrB[:, 1], s=30, c='red')
        #plt.plot(arrB[:, 0], arrB[:, 1])
        #plt.show()
    def __add__(a, b):
        """Joining 2 NURBS/BSpline by juxtaposition

        Note:
            * Adapted for second-order NURBS/BSpline.
            * The end-point of the fist NURBS/BSpline has to be the starting point of the second.


        Args:
            a (BSpline): first curve.
            b (BSpline): second curve.

        Returns:
            res (BSpline): Juxtaposition of a and b in that order.

        """
        return BSpline(np.append(a.knot[:-a.p-1], a.knot[-1] - b.knot[0] + b.knot[1:]), np.append(a.Base[:-1], b.Base, axis=0), a.p)

    def reverse(self):
        """reverse

        """
        return BSpline(self.knot[-1] - self.knot[::-1], self.Base[::-1], self.p)

    def __str__(self):
        """Use to print the NURBS/BSpline info (Knot vector and Base points) for debugging.

        Example:
            >>> myBSpline = BSpline([0, 0, 0, 1, 1, 1], [[0.3, -0.7], [1.3, -0.7], [1.3, 0.3]])
            >>> print "Hey, this is my BSpline: " + myBSpline

        """
        return "BSpline:\n - Knot Vector =\n" + str(self.knot) + "\n - Base points = \n" + str(self.Base)

    def toArray(self,nPoint=300):
        """Convert to array

        """
        knotVector = np.append(-1,self.knot)
        knotVector = map(float, knotVector)
        xi = np.linspace(self.knot[0], self.knot[-1], nPoint)
        arrB = np.array(self.Base)
        arrN = np.array([NA(knotVector, self.p, k)[1:] for k in xi])
        data = np.dot(arrN, arrB)
        data = data[range(data.shape[0]),:]
        return data
