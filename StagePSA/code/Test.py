import numpy as np
from NURBS_Class import BSpline
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.lines as lines
import matplotlib




def drawArray2D(arrBig, nx1, nx2, knot1, knot2):
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
    ax.add_collection(p)
    return


def drawWithBSpline(knot1, knot2, arrayB, p1=2, p2=2, nPoint1=25, nPoint2=25):
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
    drawArray2D(arrS, nx1, nx2, knotVector1, knotVector2)


"""""""""""""""""""""""""""""""""""
"          Test goes here         "
"""""""""""""""""""""""""""""""""""

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
"""
bigCurve = tmp + rec + tmp.reverse() + trimCurve.reverse()
bigCurve.drawCurve()
plt.xlim([-3,3])
plt.ylim([-3,3])
"""
bigB = np.concatenate(([rec.Base], [trimCurve.Base]))
drawWithBSpline(tmp.knot, rec.knot, bigB,1, 2, 15, 47)

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.show()
