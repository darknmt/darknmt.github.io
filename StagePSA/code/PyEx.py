import numpy as np
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
from NURBS import NURBSArray as RA

def drawWithNURBS(knot, arrayB, w, p=2, nPoint=200):
    knotVector = [-1] + knot
    knotVector = map(float, knotVector)
    xi = np.linspace(knot[0], knot[-1], nPoint)
    arrB = np.array(arrayB)
    arrR = [RA(knotVector, w, p, k) for k in xi]
    data = np.dot(arrR, arrB)
    data = data[range(data.shape[0]),:]
    plt.plot(data[:,0], data[:,1])
    # plt.scatter(arrB[:, 0], arrB[:, 1], s=30, c='red')
    # plt.plot(arrB[:, 0], arrB[:, 1])

def exampleNURBS():
    knot = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]
    t = 0.3
    B = [[t, 0], [t, t], [0, t], [-t, t], [-t, 0], [-t, -t], [0, -t], [t, -t], [t, 0]]
    a = np.sqrt(1.0/2)
    w = [1, a, 1, a, 1, a, 1, a, 1]
    drawWithNURBS(knot, B, w)


def main():
    #exampleBSpline()
    exampleNURBS()
    plt.plot([-1, 1, 1, -1, -1],[-1, -1, 1, 1, -1])
    plt.show()


if __name__ == "__main__":
    main()
