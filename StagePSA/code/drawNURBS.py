import numpy as np
import matplotlib.pyplot as plt
from NURBS import BSpline as N
from NURBS import BSplineArray as NA

# ------  default ------
# 50 steps for x
#
def draw(knot, p=2,nPoint=200):
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
