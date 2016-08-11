"""This module demonstrates the methode presented in a paper of Jingjing Shen
et al to quadrangulate a trimmed NURBS surface.

.. note::
        **CellPoint**, used in following the cross field is a structure of form
        **(pos, theta, ID)** where **pos** ([float, float]) is the current position, **theta** (float) is
        the angle that we arrive at current position with, ID (int) denotes the EV that
        the current branch comes from. ID is used to merge 2 different branches.


"""


import numpy as np
from NURBS_Class import BSpline
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
import random
import collections




###########################
#                         #
#   Arrays manipulation   #
#                         #
###########################




def SurfaceArray(knot1, knot2, arrayB, p1=2, p2=2, nPoint1=25, nPoint2=25):
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
    return arrS

# Input: SurfaceArray, result_Theta, Result_NbOfPass
def CrossField(arrS, arrField, arrHasValue, sqrPoint=[0,0], sqrSide=1, mode='FCFS'):
    """ Procedure to calculate the vector form of cross field based on NURBS 2D
    contour lines. We first trace these lines, each time they enter a cell, initiate
    the cross field in that cell with current direction of the entering line. There
    may exist many lines entering the same cell, in that case, if **mode** is set
    as ``normal``, average value will be used. If **mode** is set to ``FCFS``, which
    stands for `First-Come First-Served`, the first direction will be used.

    Args:
        arrS (2D float array) : output of **SurfaceArray**.
        arrField (2D [float, float] array) : initiated cross field, susceptible to change.
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).
        mode ('FCFS' or 'normal') : prefered way to pick cell direction.
    """
    N = arrField.shape[0]
    origin = np.array(sqrPoint)

    if mode=='normal':
        for i in range(arrS.shape[0]):
            for j in range(arrS.shape[1]-1):
                cutoff = map(lambda x:int(x) if int(x)!=N else int(x)-1,(arrS[i,j]-origin)*N*1.0/sqrSide)
                vect = arrS[i,j+1] - arrS[i,j]
                vect = vect/(np.linalg.norm(vect))
                arrField[cutoff[0], cutoff[1]] += vect
                arrHasValue[cutoff[0],cutoff[1]] = True
        return


    if mode=='FCFS':
        for i in range(arrS.shape[0]):
            for j in range(arrS.shape[1]-1):
                cutoff = map(lambda x:int(x) if int(x)!=N else int(x)-1,(arrS[i,j]-origin)*N*1.0/sqrSide)
                vect = arrS[i,j+1] - arrS[i,j]
                vect = vect/(np.linalg.norm(vect))
                #vect = modPi2(vect)
                if not(arrHasValue[cutoff[0], cutoff[1]]):
                    arrField[cutoff[0], cutoff[1]] = vect
                    arrHasValue[cutoff[0],cutoff[1]] = True
        return


def drawSurfaceArray(arrS):
        for i in range(arrS.shape[0]):
            plt.plot(arrS[i][:,0],arrS[i][:,1])




###########################
#                         #
#   Vector manipulation   #
#                         #
###########################




def NormalizeField(arrField, arrHasValue):
    """ Procedure to normalize a vector field

    Args:
        arrField (2D [float, float] array) : initiated cross field, susceptible to change.
        arrHasValue (2D bool array): interested domain. used to skip certain iterations.

    """
    for i in range(arrField.shape[0]):
        for j in range(arrField.shape[1]):
            if arrHasValue[i,j]:
                arrField[i,j] = arrField[i,j]/(np.linalg.norm(arrField[i,j]))
    return

#Input: EV Index
#Output: coordinates
def posFromIndex(i, j, N, sqrPoint=[0,0], sqrSide=1):
    return np.array([(i+1)*1.0/N*sqrSide, (j+1)*1.0/N*sqrSide]) + np.array(sqrPoint)

#Input: Coordinates
#Output: Cell index (real) -- To decide later
def NearestCellIndexFromPos(pos, N, sqrPoint=[0,0], sqrSide=1):
    """Function to find indices of the cell containing the current point.

    Args:
        pos ([float, float]): current point.
        N (int): number of squares in each dimension.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).

    Returns:
        ([int, int]): horizontal and vertical indices of the cell containing **pos**.

    """
    return [(pos[0]-sqrPoint[0])*N*1.0/sqrSide, (pos[1]-sqrPoint[1])*N*1.0/sqrSide]

#Input: 2 vect A,B
#Output: number of pi/2 rotation to align vect2 to vect1
def nbOfTurnField(vect1, vect2):
    """ Function calculating  the number of pi/2 turns to align a cross field with
    vector form **vect1** to one with **vect2**. It is a deprecated version of
    **nbOfTurnAngle**.

    Args:
        vect1 ([float, float]): vector form of the first cross.
        vect2 ([float, float]): vector form of the second cross.

    Returns:
        (int): number of turns.

    """
    D = np.array([[vect2[0], vect2[1]], [-vect2[1], vect2[0]], [-vect2[0], -vect2[1]], [vect2[1], -vect2[0]]])
    res = np.array([np.dot(vect1,x) for x in D])
    a = res.argmax()
    if a < 2:
        return a
    else:
        return a-4

#Input: 2 vector
#Output: distance between 2 crosses
def distField(vect1, vect2):
    """
    A vector version of **distAngle**, but deprecated.
    """
    D = np.array([[vect1[0], vect1[1]], [-vect1[1], vect1[0]]])
    res = np.array([abs(np.dot(vect2,x)) for x in D])
    return 1 - max(res)




##########################
#                        #
#   Angle manipulation   #
#                        #
##########################




#Input: float x, y
#Output: rotation until in [0,pi/2]
def modPi2(a):
    """Function that rotates a unit vector until it is in [0,pi/2].

    Args:
        a (float): angle.

    Returns:
        (float): vector after rotation.

    """
    x = a[0]
    y = a[1]
    if x*y >0:
        return np.array([abs(x),abs(y)])
    if x*y <0:
        return np.array([abs(y), abs(x)])
    return np.array([abs(x+y),0])

#Input: unit vector
#Output: angle
def angle(vect):
    """Function that convert a unit vector to angle.

    Args:
        vect ([float, float]): vector to convert.

    Returns:
        (float): the associated angle.

    """
    if vect[1] >= 0:
        return np.arccos(vect[0])
    else:
        return -np.arccos(vect[0])

#Input: 2 angle
#Output: number of pi/2 rotation to align theta2 to theta1
def nbOfTurnAngle(theta1, theta2):
    """ Function calculating  the number of pi/2 turns to align a cross field with
    angle **theta2** to one with **theta1**. It is used to calculate the index of EV.

    Args:
        theta1 (float): angle form of the first cross.
        theta2 (float): angle form of the second cross.

    Returns:
        (int): number of turns.

    """
    if (theta1-theta2)%(np.pi/2) < np.pi/4:
        return (theta1-theta2)//(np.pi/2)
    else:
        return (theta1-theta2)//(np.pi/2)+1

def distAngle(theta1, theta2):
    """Calculate the distance between 2 crosses represented by their angles.

    Example:

        The 2 cross may coincide althouth their angle are different.

        >>> distAngle(0, np.pi)
        0

        >>> distAngle(0, np.pi/2)
        0

        Note that it is not at all trivial, for example, the following result is
        pi/6, not pi/3, since the best way is to rotate counter clock-wise the first
        cross.

        >>> distAngle(pi/12, 5*np.pi/12)
        0.5235987755982988

    Args:
        theta1 (float): first angle.
        theta2 (float): second angle.

    Returns:
        res (float): angle distance between 2 crosses.

    """
    res = (theta1-theta2)%(np.pi/2)
    if res < np.pi/4:
        return res
    else:
        return np.pi/2 - res

#Input: angle [0,2pi)
#Output: distance to 0, note that dist(0,2pi) = 0
def distToZero(theta):
    """Compute the distance of an angle to 0, with modulo 2*pi.

    Args:
        theta (float) : angle to compute distance.

    Returns:
        (float): distance from theta to zero.

    """
    if theta<=np.pi:
        return theta
    else:
        return 2*np.pi - theta

def VectorToAngle(arrField, arrHasValue):
    """Function that converts vector form of cross field to angle form.

    Args:
        arrField (2D [float, float] array) : initiated cross field, susceptible to change.
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.

    Returns:
        res (2D float array): the cross field represented by an angle in [0, pi/4].

    """
    N = arrField.shape[0]
    res = np.zeros([N, N])
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                res[i,j] = angle(arrField[i,j])
    return res

def AngleToVector(arrAngleField, arrHasValue):
    """Function that converts angle form of cross field to vecto form.

    Args:
        arrAngleField (2D float array): the cross field represented by an angle in [0, pi/4].
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.

    Returns:
        res (2D [float, float] array) : initiated cross field, susceptible to change.

    """
    N = arrAngleField.shape[0]
    res = np.zeros([N, N, 2])
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                res[i,j] = np.array([np.cos(arrAngleField[i,j]), np.sin(arrAngleField[i,j])])
    return res




###########################
#                         #
#   Ploting and drawing   #
#                         #
###########################




def drawCrossFieldFromAngle(arrAngleField, arrHasValue, sqrPoint=[0,0], sqrSide=1):
    """Procedure to draw cross field with angle input.

    Args:
        arrAngleField (2D float array): the cross field represented by an angle in [0, pi/4].
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).

    """
    N = arrAngleField.shape[0]
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                pos = np.array([(i+0.5)/N*sqrSide, (j+0.5)/N*sqrSide]) + np.array(sqrPoint)
                vect = np.array([np.cos(arrAngleField[i,j]), np.sin(arrAngleField[i,j])])
                drawCross(pos, vect, sqrSide*1.0/N)

def drawCrossField(arrField, arrHasValue, sqrPoint=[0,0], sqrSide=1):
    """Procedure to draw cross field with vector input.

    Args:
        arrField (2D [float, float] array) : initiated cross field, susceptible to change.
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).

    """
    N = arrField.shape[0]
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                pos = np.array([(i+0.5)/N*sqrSide, (j+0.5)/N*sqrSide]) + np.array(sqrPoint)
                drawCross(pos, arrField[i,j], sqrSide*1.0/N)

def drawCell(N, sqrPoint=[0,0], sqrSide=1):
    """Procedure to draw grid lines that divise parametric square to N by N cells.

    Args:
        N (int): number of squares in each dimension.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).

    """
    for i in range(N-1):
        lineUp([sqrPoint[0]+(1+i)*sqrSide*1.0/N,sqrPoint[1]], [sqrPoint[0]+(1+i)*sqrSide*1.0/N,sqrPoint[1]+sqrSide],'black')
        lineUp([sqrPoint[0], sqrPoint[1]+(1+i)*sqrSide*1.0/N], [sqrPoint[0]+sqrSide, sqrPoint[1]+(1+i)*sqrSide*1.0/N], 'black')

def drawCellCenter(N, sqrPoint=[0,0], sqrSide=1):
    """Procedure to draw grid lines that pass by centers of cells.
    It is used to manually construct and check the cross field.

    Args:
        N (int): number of cells in each dimension.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).

    """
    for i in range(N):
        lineUp([sqrPoint[0]+(0.5+i)*sqrSide*1.0/N,sqrPoint[1]], [sqrPoint[0]+(0.5+i)*sqrSide*1.0/N,sqrPoint[1]+sqrSide],'black')
        lineUp([sqrPoint[0], sqrPoint[1]+(0.5+i)*sqrSide*1.0/N], [sqrPoint[0]+sqrSide, sqrPoint[1]+(0.5+i)*sqrSide*1.0/N], 'black')

def lineUp(first,second, c='red', lw=0.5):
    """Procedure to draw a line connecting 2 points.

        Args:
            first ([float, float]): first ending point.
            second ([float, float]): second ending point.
            c (color): color of the line (default='red').
            lw (float): line width (default=0.5).

    """
    plt.plot([first[0],second[0]], [first[1], second[1]], color=c, linewidth=lw)

def drawCross(pos, vect, side):
    """Procedure to draw a cross with size relative to the cell containing it.

    Args:
        pos ([float, float]): coordinate of the center of the cross.
        vect ([float, float]): one of 4 vectors that represent the cross.
        side (float) : side of a square which contain the cross.

    """
    a = vect*side*1.0/5
    b = np.array([-a[1],a[0]])
    lineUp((pos + a), (pos-a), 'red', lw=2)
    lineUp(pos +b, pos - b, 'green', lw=2)
    return


###########################################
#                                         #
#   Extraordinary vertices manipulation   #
#                                         #
###########################################




def cutOffDirection(arr, nbRemain):
    """Function that clusters directions in **arr** to **nbRemain** group.

    Args:
        arr (float array): array of directions in form of angles, susceptible to change.
        nbRemain (int): number of direction to keep, calculated from the index of Extraordinary Vertex.

    Returns:
        arr (float array): new array of exactly **nbRemain** angles.

    """
    while len(arr) > nbRemain:
        minDiff = arr[0] - arr[-1]+ 2*np.pi
        k = -1
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < minDiff:
                minDiff = arr[i+1] - arr[i]
                k = i
        arr[k] = 0.5*(arr[k] + arr[k+1])
        del arr[k+1]
    return arr

#Input: arrive at pos with angle theta
#Output: decide which point to go, with which angle
def expandByFieldNonEV(point, arrAngleField, arrHistory, arrHasValue, dequeue, sqrPoint=[0,0], sqrSide=1):
    """Function that calculates the new CellPoint from the current CellPoint and
    keeps dequeue up-to-date.

    Args:
        point (CellPoint): current CellPoint.
        arrAngleField (2D float array): the cross field represented by an angle in [0, pi/4].
        arrHistory (2D array of PointCell set): array keeping trace of all CellPoint that already arrived in a cell, used to merge different branches, susceptible to change.
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.
        dequeue (Python deque): double-ended queue of CellPoint, used in cell browsing and following cross field, susceptible to change.
        sqrPoint ([float, float]): left-lower corner of parametric square (default=[0,0]).
        sqrSide (float) : side length of parametric square (default=1).

    Returns:
        (CellPoint): new CellPoint to browse, already added to **dequeue**. ``None`` if branches merged or boundary reached.

    """
    #Where am I
    pos, theta, ID = point
    N = arrHasValue.shape[0]
    a = sqrSide*1.0/N
    [i, j] = NearestCellIndexFromPos(pos, N, sqrPoint, sqrSide)
    if (i >N-0.1) or (i<0) or (j>N-0.1) or (j <0):
        return None
    i =int(i)
    j = int(j)


    if not(arrHasValue[i,j]):
        return None

    #Remove local points from queue, if there are any
    for ind in range(len(dequeue)):
        dequeuePoint = dequeue[ind]
        if dequeuePoint[-1] != ID:
            iDP, jDP = map(int,NearestCellIndexFromPos(dequeuePoint[0], N, sqrPoint, sqrSide))
            if abs(iDP-i)<2 and abs(jDP-j)<2:
                lineUp(pos,dequeuePoint[0], c='blue', lw=2.5)
                del dequeue[ind]
                return None

    #Search for Local Points in History and connect to it

    #For debugging purposes
    # if(arrHistory[i][j] != []) and arrHistory[i][j][0][-1] != ID:
    #     dist = 2*a;
    #     for p in arrHistory[i][j]:
    #         tmp = np.linalg.norm(p[0]-pos)
    #         if tmp<dist:
    #             localpos = p[0]
    #             dist = tmp
    #     lineUp(pos,localpos, c='blue', lw=1.5)
    #     #search and remove localpos from deque
    #     for tmp in dequeue:
    #         if (tmp[0] == localpos).all():
    #             dequeue.remove(tmp)
    #     return None
    checkCell = []
    for i1 in range(i-1, i+2):
        for j1 in range(j-1, j+2):
            if (i1>=0) and (i1<N) and (j1>=0) and (j1<N) and (arrHistory[i1][j1] != []) and (arrHistory[i1][j1][0][-1] != ID):
                checkCell = checkCell + arrHistory[i1][j1]
    # For Debugging purposes
    # if (i<N-1) and arrHistory[i+1][j] != [] and arrHistory[i+1][j][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i+1][j]
    # if j<N-1 and arrHistory[i][j+1] != [] and arrHistory[i][j+1][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i][j+1]
    # if i>0 and arrHistory[i-1][j] != [] and arrHistory[i-1][j][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i-1][j]
    # if j>0 and arrHistory[i][j-1] != [] and arrHistory[i][j-1][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i][j-1]
    # #Stupidity!!!
    # if (i<N-1 and j<N-1) and arrHistory[i+1][j+1] != [] and arrHistory[i+1][j+1][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i+1][j+1]
    # if (i>0 and j<N-1) and arrHistory[i-1][j+1] != [] and arrHistory[i-1][j+1][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i-1][j+1]
    # if (i<N-1 and j>0) and arrHistory[i+1][j-1] != [] and arrHistory[i+1][j-1][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i+1][j-1]
    # if (i>0 and j>0) and arrHistory[i-1][j-1] != [] and arrHistory[i-1][j-1][0][-1] != ID:
    #     checkCell = checkCell + arrHistory[i-1][j-1]

    if checkCell != []:
        #Line Up
        #dist = 3*a
        dist = 6*a
        for p in checkCell:
            tmp = np.linalg.norm(p[0]-pos)
            if tmp<dist:
                localpos = p[0]
                dist = tmp
        #search and remove localpos from deque
        lineUp(pos,localpos, c='blue', lw=1.5)
        for tmp in dequeue:
            if (tmp[0] == localpos).all():
                dequeue.remove(tmp)
        return None

    arrHistory[i][j].append(point)
    dir = np.array([arrAngleField[i,j], arrAngleField[i,j] + 0.5*np.pi, arrAngleField[i,j] + np.pi, arrAngleField[i,j] + 1.5*np.pi])
    test = np.vectorize(distToZero)((dir-theta)%(2*np.pi))
    newTheta = dir[test.argmin()]
    if abs(np.cos(newTheta))<TOL:
        t1 = -1
    elif (pos[0]/a-0.5)%1 < TOL or (pos[0]/a-0.5)%1 > 1-TOL :
        t1 = a/abs(np.cos(newTheta));
    elif np.cos(newTheta)>0:
        t1 = ((0.5*a-pos[0])%a)/np.cos(newTheta)
    else:
        t1 = -((pos[0] - 0.5*a)%a)/np.cos(newTheta)

    if abs(np.sin(newTheta))<TOL:
        t2 = -1
    elif (pos[1]/a-0.5)%1 < TOL or (pos[1]/a-0.5)%1 > 1-TOL:
        t2 = a/abs(np.sin(newTheta));
    elif np.sin(newTheta)>0:
        t2 = ((0.5*a-pos[1])%a)/np.sin(newTheta)
    else:
        t2 = -((pos[1] - 0.5*a)%a)/np.sin(newTheta)

    if t1==-1:
        t=t2
    elif t2==-1:
        t=t1
    else:
        t = min(t1, t2)

    if (abs(t1-t2) < TOL):
        newPos = pos + np.array([t1*np.cos(newTheta), t2*np.sin(newTheta)])
    else:
        newPos =pos + t*np.array([np.cos(newTheta), np.sin(newTheta)])
    lineUp(pos,newPos, c='blue', lw=1.5)
    return (newPos, newTheta, ID)




####################################
#                                  #
#   Metropolis-Hastings algorithm  #
#                                  #
####################################




def MetropolisHastings(arrAngleField, arrHasValue, NbIter=100000, initBeta=1., incBeta=5.):
    """ Implementation of Metropolis-Hasting algorithm

    Args:
        arrAngleField (2D float array): the cross field represented by an angle in [0, pi/4].
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.
        NbIter (int): numer of iterations (default=100000).
        initBeta (float): initial value for parameter **beta** (inverse of temperature).
        incBeta (float): increment in **beta**.

    Warning:
        This procedure may yield difficulty in debugging, and may not converge at all.

    """
    N = arrHasValue.shape[0]
    beta = initBeta
    step = float(incBeta)/NbIter
    #coeff = pow(np.pi,2)/8
    for k in range(NbIter):
        i = random.randint(1,N-2) # Eviter le bord
        j = random.randint(1,N-2)
        #beta = beta + step
        beta = beta + (step*(2*k+1))/NbIter

        if arrHasValue[i,j] and arrHasValue[i-1,j] and arrHasValue[i+1,j] and arrHasValue[i,j+1] and arrHasValue[i,j-1] and arrHasValue[i+1,j+1] and arrHasValue[i-1,j-1] and arrHasValue[i+1,j-1] and arrHasValue[i-1,j+1]:
            #Update arrField[i,j]
            #Restraint
            #theta = random.uniform(-np.pi/2,np.pi/2)
            #theta = arrAngleField[i,j] + theta
            #Free
            theta = random.uniform(-np.pi,np.pi)

            #Calculate Energie of 2 configs.
            E1 = pow(distAngle(arrAngleField[i,j], arrAngleField[i+1,j]), 2) + pow(distAngle(arrAngleField[i,j], arrAngleField[i,j+1]), 2) + \
                    pow(distAngle(arrAngleField[i,j], arrAngleField[i-1,j]), 2) + pow(distAngle(arrAngleField[i,j], arrAngleField[i, j-1]), 2)

            E2 = pow(distAngle(theta, arrAngleField[i+1,j]), 2) + pow(distAngle(theta, arrAngleField[i,j+1]), 2) + \
                    pow(distAngle(theta, arrAngleField[i-1,j]), 2) + pow(distAngle(theta, arrAngleField[i, j-1]), 2) #+ \

            if E2<E1:
                arrAngleField[i,j] = theta
            else:
                prob = random.uniform(0,1)
                if prob < np.exp(-beta*(E2 - E1)):
                    arrAngleField[i,j] = theta




######################################
#                                    #
#           Main algorithm           #
#                                    #
######################################




def mainAlgorithm():
    """ Main algorithm

    Args:
        N: number of cells in each dimension
        arrField (2D [float, float] array) : initiated cross field, susceptible to change.
        arrAngleField (2D float array): the cross field as array of angles in [0, pi/4].
        arrHasValue (2D bool array): **arrHasValue[i,j]** = ``True`` if and only if the cell [i,j] lies in the trimmed domain.
        arrIndex (2D int array): array of cell index, used to detect Extraordinary Vertices.
        EV (point set): set of Extraordinary Vertices.
        dequeue (Python deque): double-ended queue of CellPoint, used in cell browsing and following cross field.

    Returns:
        test.png (file) : PNG image file and screen output

    """
    ######################################
    #                                    #
    #   Draw square and trimming curve   #
    #                                    #
    ######################################
    #draw square
    a = BSpline([0, 0, 0, 1, 1, 1], [[2, 2], [0, 2], [-2, 2]])
    b = BSpline([0, 0, 0, 1, 1, 1], [[2, -2], [2, 0], [2, 2]])
    c = BSpline([0, 0, 0, 1, 1, 1], [[-2, -2], [0, -2], [2, -2]])
    d = BSpline([0, 0, 0, 1, 1, 1], [[-2, 2], [-2, 0], [-2, -2]])
    rec = b+a+d+c
    rec.drawCurve(c='blue', lw=1.5)
    sqrPoint=[-2,-2]
    sqrSide=4

    #draw trimming curve
    psing1 = np.array([0.3, -0.7])
    psing2 = np.array([2, -2])
    a = BSpline([0, 0, 0, 1, 1, 1], [psing1, [1.3, -0.7], [1.3, 0.3]])
    b = BSpline([0, 0, 0, 1, 1, 1], [[1.3, 0.3], [1.3, 1.3], [0.3, 1.3]])
    c = BSpline([0, 0, 0, 1, 1, 1], [[0.3, 1.3], [-0.7, 1.3], [-0.7, 0.3]])
    d = BSpline([0, 0, 0, 1, 1, 1], [[-0.7, 0.3], [-0.7, -0.7], psing1])
    trimCurve = a+b+c+d
    trimCurve.drawCurve(c='blue', lw=1.5)

    tmp = BSpline([0,0,1,1], [psing1, psing2])
    #tmp.drawCurve()
    bigB = np.concatenate(([rec.Base], [trimCurve.Base]))
    arrS = SurfaceArray(tmp.knot, rec.knot, bigB,1, 2, 60, 501)

    #Draw Level Curve
    #drawSurfaceArray(arrS)




    ##################################
    #                                #
    #   Initiate fields and arrays   #
    #                                #
    ##################################
    #Number of squares in each dimension
    N = 28
    arrField = np.zeros([N, N, 2])
    arrIndex = np.zeros([N-1, N-1])
    arrHasValue = [[False for j in range(N)] for i in range(N)]
    arrHasValue = np.array(arrHasValue)

    #Set of extraordinary vertices
    EV = {}

    #Tolerance in floating point manipulation
    TOL = 1e-5



    ############################################
    #                                          #
    #   Calculate and manipulate cross field   #
    #                                          #
    ############################################
    #Calculate cross field
    CrossField(arrS, arrField, arrHasValue, sqrPoint=sqrPoint, sqrSide=sqrSide, mode='FCFS')

    #Normalize cross field
    NormalizeField(arrField, arrHasValue)
    arrHistory = [[[] for j in range(N)] for i in range(N)]

    #Convert cross field from vector field to angle field
    arrAngleField = VectorToAngle(arrField, arrHasValue)




    ################################
    #                              #
    #   Apply Metropolis-Hasting   #
    #                              #
    ################################
    #MetropolisHastings(arrAngleField, arrHasValue, NbIter=500, initBeta=10)




    #######################################
    #                                     #
    #   Calculate Index and Singularity   #
    #                                     #
    #######################################
    dequeue = collections.deque()
    ID = 0
    print "---\nSingular points: \n"
    for i in range(N-1):
        for j in range(N-1):
            if arrHasValue[i,j] and arrHasValue[i,j] and arrHasValue[i+1,j] and arrHasValue[i+1,j+1] and arrHasValue[i,j+1]:
                arrIndex[i,j] = nbOfTurnAngle(arrAngleField[i,j], arrAngleField[i+1,j]) + nbOfTurnAngle(arrAngleField[i+1,j], arrAngleField[i+1,j+1]) + \
                                nbOfTurnAngle(arrAngleField[i+1,j+1],arrAngleField[i,j+1]) + nbOfTurnAngle(arrAngleField[i,j+1],arrAngleField[i,j])
                arrIndex[i,j] = arrIndex[i,j]%4
                if arrIndex[i,j] !=0:
                    pos = posFromIndex(i, j, N, sqrPoint=[-2,-2], sqrSide=4)
                    plt.scatter(pos[0], pos[1], s=30, c='blue')
                    EV = []

                    tmp=(0.5*arrAngleField[i,j] + 0.5*arrAngleField[i+1,j] + np.pi/4*nbOfTurnAngle(arrAngleField[i,j], arrAngleField[i+1,j]))%(2*np.pi)
                    if tmp<np.pi:
                        tmp = (tmp+np.pi)%(2*np.pi)
                    EV.append(tmp)
                    tmp = (tmp + 0.5*np.pi)%(2*np.pi)
                    if tmp<np.pi:
                        tmp = (tmp+np.pi)%(2*np.pi)
                    EV.append(tmp)


                    tmp = (0.5*arrAngleField[i+1,j] + 0.5*arrAngleField[i+1,j+1] + np.pi/4*nbOfTurnAngle(arrAngleField[i+1,j], arrAngleField[i+1,j+1]))%(2*np.pi)
                    if (tmp > 0.5*np.pi) and (tmp < 1.5*np.pi):
                        tmp = (tmp + np.pi)%(2*np.pi)
                    EV.append(tmp)
                    tmp = (tmp + 0.5*np.pi)%(2*np.pi)
                    if (tmp > 0.5*np.pi) and (tmp < 1.5*np.pi):
                        tmp = (tmp + np.pi)%(2*np.pi)
                    EV.append(tmp)

                    tmp = (0.5*arrAngleField[i+1,j+1] + 0.5*arrAngleField[i,j+1] +  np.pi/4*nbOfTurnAngle(arrAngleField[i+1,j+1], arrAngleField[i,j+1]))%(2*np.pi)
                    if tmp > np.pi:
                        tmp = tmp - np.pi
                    EV.append(tmp)
                    tmp = (tmp + 0.5*np.pi)%(2*np.pi)
                    if tmp > np.pi:
                        tmp = tmp - np.pi
                    EV.append(tmp)

                    tmp = (0.5*arrAngleField[i,j+1] + 0.5*arrAngleField[i,j] + np.pi/4*nbOfTurnAngle(arrAngleField[i,j+1], arrAngleField[i,j]))%(2*np.pi)
                    if (tmp < 0.5*np.pi) or (tmp > 1.5*np.pi):
                        tmp = (tmp + np.pi)%(2*np.pi)
                    EV.append(tmp)
                    tmp = (tmp + 0.5*np.pi)%(2*np.pi)
                    if (tmp < 0.5*np.pi) or (tmp > 1.5*np.pi):
                        tmp = (tmp + np.pi)%(2*np.pi)
                    EV.append(tmp)
                    EV.sort()
                    cutOffDirection(EV, arrIndex[i,j]+2)

                    arrHistory[i][j].append((pos,0,ID))
                    arrHistory[i+1][j].append((pos,0,ID))
                    arrHistory[i][j+1].append((pos,0,ID))
                    arrHistory[i+1][j+1].append((pos,0,ID))

                    a = sqrSide*1.0/N
                    for theta in EV:
                        if np.cos(theta)==0:
                            t1 = -1
                        elif np.cos(theta)>0:
                            t1 = ((0.5*a-pos[0])%a)/np.cos(theta)
                        else:
                            t1 = -((pos[0] - 0.5*a)%a)/np.cos(theta)

                        if np.sin(theta)==0:
                            t2 = -1
                        elif np.sin(theta)>0:
                            t2 = ((0.5*a-pos[1])%a)/np.sin(theta)
                        else:
                            t2 = -((pos[1] - 0.5*a)%a)/np.sin(theta)

                        if t1==-1:
                            t=t2
                        elif t2==-1:
                            t=t1
                        else:
                            t = min(t1, t2)

                        newPos=pos + t*np.array([np.cos(theta), np.sin(theta)])
                        lineUp(pos,newPos,c='blue', lw=1.5)
                        dequeue.append((newPos,theta, ID))

                    print "\tarrIndex[" + str(i) + ", " + str(j) + "] = " + str(arrIndex[i,j])
                    print nbOfTurnAngle(arrAngleField[i,j], arrAngleField[i+1,j])
                    print nbOfTurnAngle(arrAngleField[i+1,j], arrAngleField[i+1,j+1])
                    print nbOfTurnAngle(arrAngleField[i+1,j+1],arrAngleField[i,j+1])
                    print nbOfTurnAngle(arrAngleField[i,j+1],arrAngleField[i,j])
                    print "\n"
                    ID +=1
    print dequeue
    print "\nEnd of data\n"




    ######################################
    #                                    #
    #   Continue to follow Cross Field   #
    #                                    #
    ######################################
    while dequeue:
        currentPoint = dequeue.popleft()
        res = expandByFieldNonEV(currentPoint, arrAngleField, arrHistory, arrHasValue, dequeue, sqrPoint=sqrPoint, sqrSide=sqrSide)
        print res
        if res != None:
            dequeue.append(res)



    #####################################
    #                                   #
    #   Drawing cells and cross Field   #
    #                                   #
    #####################################
    drawCell(N, sqrPoint=sqrPoint, sqrSide=sqrSide)
    #Draw Cross Field
    drawCrossFieldFromAngle(arrAngleField, arrHasValue, sqrPoint=sqrPoint, sqrSide=sqrSide)

    #Set coordinate
    plt.xlim([sqrPoint[0]-1,sqrPoint[0]+sqrSide+1])
    plt.ylim([sqrPoint[1]-1,sqrPoint[1]+sqrSide+1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig('test.png')
    plt.show()

if __name__ == "__main__":
    mainAlgorithm()
