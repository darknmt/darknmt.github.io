import numpy as np
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
from NURBS import NURBSArray as RA
import matplotlib.cm as cm
from matplotlib.collections import LineCollection


def drawWithBSpline(knot, arrayB, p=2, nPoint=300, pControl=False):
    #[0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]
    knotVector = np.append(-1, knot)
    knotVector = map(float, knotVector)
    #iMax = len(knotVector) - 1 - p
    xi = np.linspace(knot[0], knot[-1], nPoint)
    arrB = np.array(arrayB)
    arrN = np.array([NA(knotVector, p, k)[1:] for k in xi])
    data = np.dot(arrN, arrB)
    data = data[range(data.shape[0]),:]
    plt.plot(data[:,0], data[:,1])
    if pControl:
        plt.scatter(arrB[:, 0], arrB[:, 1], s=30, c='red')
        plt.plot(arrB[:, 0], arrB[:, 1])
    plt.show()

def drawWithNURBS(knot, arrayB, w, p=2, nPoint=300):
    knotVector = np.append(-1, knot)
    knotVector = map(float, knotVector)
    xi = np.linspace(knot[0], knot[-1], nPoint)
    arrB = np.array(arrayB)
    arrR = [RA(knotVector, w, p, k) for k in xi]
    data = np.dot(arrR, arrB)
    data = data[range(data.shape[0]),:]
    plt.plot(data[:,0], data[:,1])
    plt.scatter(arrB[:, 0], arrB[:, 1], s=30, c='red')
    plt.plot(arrB[:, 0], arrB[:, 1])
    plt.show()

def exampleBSpline():
    knot = [0., 0., 0., 1., 2., 3., 4., 4., 5., 5., 5.]
    knot = np.array(map(float,knot))
    knot = knot / knot[-1]
    B = [[0, 1], [1, 0], [2, 0], [2, 2], [4, 2], [5, 4], [2, 5], [1, 3]]
    drawWithBSpline(knot, B)

def randomBSpline():
    numPoint = 550
    numBreak = 350
    knot = np.random.rand(numPoint-3)
    knot.sort()
    knot = np.append([0.0, 0.0, 0.0], knot)
    knot = np.append(knot, [1.0, 1.0, 1.0])
    knot = map(int, numBreak*knot)
    print "Knot vector = \n" + str(knot) + "\n"
    knot = list(knot)
    B = np.random.rand(numPoint, 2)
    B = list(B)
    print "Control points = \n"
    for x in B:
        print x
    #plt.scatter([B[0,0], B[-1,0]], [B[0,1], B[-1,1]], s=30, c='red')
    drawWithBSpline(knot, B, p=2,nPoint=1900)

"""
^_^        ^_^       COLORFUL       ^_^       ^_^
"""

def drawWithBSplineColorful(knot, arrayB, p=2, nPoint=300, pControl=False):
    #[0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]
    knotVector = np.append(-1, knot)
    knotVector = map(float, knotVector)
    #iMax = len(knotVector) - 1 - p
    xi = np.linspace(knot[0], knot[-1], nPoint)
    arrB = np.array(arrayB)
    arrN = np.array([NA(knotVector, p, k)[1:] for k in xi])
    data = np.dot(arrN, arrB)
    data = data[range(data.shape[0]),:]
    cmap = plt.get_cmap('Blues')
    plt.xlim((0.2,0.8))
    plt.ylim((0.2,0.8))

    #plt.plot(data[:,0], data[:,1])
    i=0
    for start, stop in zip(data[:-1], data[1:]):
        x, y = zip(start,stop)
        plt.plot(x,y, color=cmap(i*1.0/nPoint), linewidth=1)
        i +=1
    """
    points = data.reshape(-1,1,2)
    segments = np.concatenate([points[:-1], points[1:]],axis=1)
    lc = LineCollection(segments,cmap=cmap, norm=plt.Normalize(0,10))
    plt.gca().add_collection(lc)
    """
    if pControl:
        plt.scatter(arrB[:, 0], arrB[:, 1], s=30, c='red')
        plt.plot(arrB[:, 0], arrB[:, 1])
    plt.savefig('Vebay.png', format='png', dpi=1600)
    plt.show()

def randomBSplineColorful():
    numPoint = 260
    numBreak = 100
    knot = np.random.rand(numPoint-3)
    knot.sort()
    knot = np.append([0.0, 0.0, 0.0], knot)
    knot = np.append(knot, [1.0, 1.0, 1.0])
    knot = map(int, numBreak*knot)
    print "Knot vector = \n" + str(knot) + "\n"
    knot = list(knot)
    B = np.random.rand(numPoint, 2)
    B = list(B)
    print "Control points = \n"
    for x in B:
        print x
    #plt.scatter([B[0,0], B[-1,0]], [B[0,1], B[-1,1]], s=30, c='red')
    drawWithBSplineColorful(knot, B, p=2,nPoint=3000)


def exampleCloseBSpline():
    knot = [0, 0, 0, 2, 2, 2]
    B = [[0, 0], [1, 2], [-1, 1]]
    drawWithBSpline(knot, B)


def exampleNURBS():
    knot = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4]
    B = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0]]
    a = np.sqrt(1.0/2)
    w = [1, a, 1, a, 1, a, 1, a, 1]
    drawWithNURBS(knot, B, w)


def main():
    #exampleBSpline()
    #exampleNURBS()
    #randomBSpline()
    randomBSplineColorful()
    #exampleCloseBSpline()

if __name__ == "__main__":
    main()
