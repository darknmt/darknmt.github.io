import numpy as np
from NURBS_Class import BSpline
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
import random
import collections

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

#Input: float x, y
#Output: rotation until in [0,pi/2]
def modPi2(a):
    x = a[0]
    y = a[1]
    if x*y >0:
        return np.array([abs(x),abs(y)])
    if x*y <0:
        return np.array([abs(y), abs(x)])
    return np.array([abs(x+y),0])

# Input: SurfaceArray, result_Theta, Result_NbOfPass
def CrossField(arrS, arrField, arrHasValue, sqrPoint=[0,0], sqrSide=1, mode='normal'):
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

"""
---------------------------------------------- Vector ----------------------------------------------
"""

def NormalizeField(arrField, arrHasValue):
    for i in range(arrField.shape[0]):
        for j in range(arrField.shape[1]):
            if arrHasValue[i,j]:
                arrField[i,j] = arrField[i,j]/(np.linalg.norm(arrField[i,j]))
    return

def lineUp(a,b, c='red', lw=0.5):
    plt.plot([a[0],b[0]], [a[1], b[1]], color=c, linewidth=lw)

def drawCross(pos, vect, side):
    a = vect*side*1.0/5
    b = np.array([-a[1],a[0]])
    lineUp((pos + a), (pos-a), 'red', lw=2)
    lineUp(pos +b, pos - b, 'green', lw=2)
    return

#Input: EV Index
#Output: coordinates
def posFromIndex(i, j, N, sqrPoint=[0,0], sqrSide=1):
    return np.array([(i+1)*1.0/N*sqrSide, (j+1)*1.0/N*sqrSide]) + np.array(sqrPoint)

#Input: Coordinates
#Output: Cell index (real) -- To decide later
def NearestCellIndexFromPos(pos, N, sqrPoint=[0,0], sqrSide=1):
    return [(pos[0]-sqrPoint[0])*N*1.0/sqrSide, (pos[1]-sqrPoint[1])*N*1.0/sqrSide]

def drawCrossField(arrField, arrHasValue, sqrPoint=[0,0], sqrSide=1):
    N = arrField.shape[0]
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                pos = np.array([(i+0.5)/N*sqrSide, (j+0.5)/N*sqrSide]) + np.array(sqrPoint)
                drawCross(pos, arrField[i,j], sqrSide*1.0/N)

def drawCell(N, sqrPoint=[0,0], sqrSide=1):
    for i in range(N-1):
        lineUp([sqrPoint[0]+(1+i)*sqrSide*1.0/N,sqrPoint[1]], [sqrPoint[0]+(1+i)*sqrSide*1.0/N,sqrPoint[1]+sqrSide],'black')
        lineUp([sqrPoint[0], sqrPoint[1]+(1+i)*sqrSide*1.0/N], [sqrPoint[0]+sqrSide, sqrPoint[1]+(1+i)*sqrSide*1.0/N], 'black')


def drawCellCenter(N, sqrPoint=[0,0], sqrSide=1):
    for i in range(N):
        lineUp([sqrPoint[0]+(0.5+i)*sqrSide*1.0/N,sqrPoint[1]], [sqrPoint[0]+(0.5+i)*sqrSide*1.0/N,sqrPoint[1]+sqrSide],'black')
        lineUp([sqrPoint[0], sqrPoint[1]+(0.5+i)*sqrSide*1.0/N], [sqrPoint[0]+sqrSide, sqrPoint[1]+(0.5+i)*sqrSide*1.0/N], 'black')

#Input: 2 vect A,B
#Output: number of pi/2 rotation to align vect2 to vect1
def nbOfTurnField(vect1, vect2):
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
    D = np.array([[vect1[0], vect1[1]], [-vect1[1], vect1[0]]])
    res = np.array([abs(np.dot(vect2,x)) for x in D])
    return 1 - max(res)

"""
---------------------------------------------- Angle ----------------------------------------------
"""

#Input: unit vector
#Output: angle
def angle(vect):
    if vect[1] >= 0:
        return np.arccos(vect[0])
    else:
        return -np.arccos(vect[0])

#Input: 2 angle
#Output: number of pi/2 rotation to align theta2 to theta1
def nbOfTurnAngle(theta1, theta2):
    if (theta1-theta2)%(np.pi/2) < np.pi/4:
        return (theta1-theta2)//(np.pi/2)
    else:
        return (theta1-theta2)//(np.pi/2)+1

def distAngle(theta1, theta2):
    res = (theta1-theta2)%(np.pi/2)
    if res < np.pi/4:
        return res
    else:
        return np.pi/2 - res

#Input: angle [0,2pi)
#Output: distance to 0, note that dist(0,2pi) = 0
def distToZero(theta):
    if theta<=np.pi:
        return theta
    else:
        return 2*np.pi - theta

def VectorToAngle(arrField, arrHasValue):
    N = arrField.shape[0]
    res = np.zeros([N, N])
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                res[i,j] = angle(arrField[i,j])
    return res

def AngleToVector(arrAngleField, arrHasValue):
    N = arrAngleField.shape[0]
    res = np.zeros([N, N, 2])
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                res[i,j] = np.array([np.cos(arrAngleField[i,j]), np.sin(arrAngleField[i,j])])
    return res

def drawCrossFieldFromAngle(arrAngleField, arrHasValue, sqrPoint=[0,0], sqrSide=1):
    N = arrAngleField.shape[0]
    for i in range(N):
        for j in range(N):
            if arrHasValue[i,j]:
                pos = np.array([(i+0.5)/N*sqrSide, (j+0.5)/N*sqrSide]) + np.array(sqrPoint)
                vect = np.array([np.cos(arrAngleField[i,j]), np.sin(arrAngleField[i,j])])
                drawCross(pos, vect, sqrSide*1.0/N)

def cutOffDirection(arr, nbRemain):
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

#Note arrHistory = arrHasValue, AND is FALSE ON BOUNDARY
#Point = (pos, theta, ID)
def expandByFieldNonEV(point, arrAngleField, arrHistory, N, sqrPoint=[0,0], sqrSide=1):
    #Where am I
    pos, theta, ID = point
    a = sqrSide*1.0/N
    [i, j] = NearestCellIndexFromPos(pos, N, sqrPoint, sqrSide)
    if (i >N) or (i<0) or (j>N) or (j <0):
        return None
    i =int(i)
    j = int(j)

    if(arrHistory[i,j] != ID and arrHistory[i,j]!=-1) or (arrHistory[i,j] == -2):
        return None
    elif (arrHistory[i,j]==-1):
        arrHistory[i,j] = ID

    dir = np.array([arrAngleField[i,j], arrAngleField[i,j] + 0.5*np.pi, arrAngleField[i,j] + np.pi, arrAngleField[i,j] + 1.5*np.pi])
    test = np.vectorize(distToZero)((dir-theta)%(2*np.pi))
    newTheta = dir[test.argmin()]
    if abs(np.cos(newTheta))<1e-2:
        t1 = -1
    elif (pos[0]/a-0.5)%1 < 1e-2 or (pos[0]/a-0.5)%1 > 1-1e-2 :
        t1 = a/abs(np.cos(newTheta));
    elif np.cos(newTheta)>0:
        t1 = ((0.5*a-pos[0])%a)/np.cos(newTheta)
    else:
        t1 = -((pos[0] - 0.5*a)%a)/np.cos(newTheta)

    if abs(np.sin(newTheta))<1e-2:
        t2 = -1
    elif (pos[1]/a-0.5)%1 < 1e-2 or (pos[1]/a-0.5)%1 > 1-1e-2:
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

    newPos =pos + t*np.array([np.cos(newTheta), np.sin(newTheta)])
    lineUp(pos,newPos, c='blue', lw=1.5)
    return (newPos, newTheta, ID)


"""
"""""""""""""""""""""""""""""""""""""""
"""          Test goes here         """
"""""""""""""""""""""""""""""""""""""""
"""
#draw square
a = BSpline([0, 0, 0, 1, 1, 1], [[2, 2], [0, 2], [-2, 2]])
b = BSpline([0, 0, 0, 1, 1, 1], [[2, -2], [2, 0], [2, 2]])
c = BSpline([0, 0, 0, 1, 1, 1], [[-2, -2], [0, -2], [2, -2]])
d = BSpline([0, 0, 0, 1, 1, 1], [[-2, 2], [-2, 0], [-2, -2]])
rec = b+a+d+c
rec.drawCurve()

#draw trimming curve

psing1 = np.array([0.3, -0.7])
psing2 = np.array([2, -2])
a = BSpline([0, 0, 0, 1, 1, 1], [psing1, [1.3, -0.7], [1.3, 0.3]])
b = BSpline([0, 0, 0, 1, 1, 1], [[1.3, 0.3], [1.3, 1.3], [0.3, 1.3]])
c = BSpline([0, 0, 0, 1, 1, 1], [[0.3, 1.3], [-0.7, 1.3], [-0.7, 0.3]])
d = BSpline([0, 0, 0, 1, 1, 1], [[-0.7, 0.3], [-0.7, -0.7], psing1])
trimCurve = a+b+c+d
trimCurve.drawCurve()

tmp = BSpline([0,0,1,1], [psing1, psing2])
#tmp.drawCurve()


bigB = np.concatenate(([rec.Base], [trimCurve.Base]))
arrS = SurfaceArray(tmp.knot, rec.knot, bigB,1, 2, 60, 501)

#Draw Level Curve
#drawSurfaceArray(arrS)

N = 30
arrField = np.zeros([N, N, 2])
arrIndex = np.zeros([N-1, N-1])
arrHasValue = [[False for j in range(N)] for i in range(N)]
arrHasValue = np.array(arrHasValue)
EV = {}
CrossField(arrS, arrField, arrHasValue, sqrPoint=[-2,-2], sqrSide=4, mode='FCFS')

NormalizeField(arrField, arrHasValue)
arrHistory = np.zeros([N,N],dtype=np.int)
for i in range(N):
    for j in range(N):
        if arrHasValue[i,j]:
            arrHistory[i,j] = -1
        else:
            arrHistory[i,j] = -2 #already passed

#Inintiate Angle Field
arrAngleField = VectorToAngle(arrField, arrHasValue)

"""
---------------------------------------------- Metropolis-Hastings ----------------------------------------------

NbIter = 200000
beta = 3
step = 5.0/NbIter
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

---------------------------------------------- Calculate Index and Singularity ----------------------------------------------
"""

dequeue = collections.deque()
sqrPoint=[-2,-2]
sqrSide=4
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
                #print np.array(EV)/np.pi
                #print np.array(cutOffDirection(EV, arrIndex[i,j]+2))/np.pi
                cutOffDirection(EV, arrIndex[i,j]+2)

                arrHistory[i,j]=ID
                arrHistory[i+1,j]=ID
                arrHistory[i,j+1]=ID
                arrHistory[i+1,j+1]=ID

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


"""Continue to follow Cross Field"""
print dequeue
print "\nEnd of data\n"
while dequeue:
    currentPoint = dequeue.popleft()
    res = expandByFieldNonEV(currentPoint, arrAngleField, arrHistory, N, sqrPoint=[-2,-2], sqrSide=4)
    print res
    if res != None:
        dequeue.append(res)




"""
---------------------------------------------- Draw Vector Field ----------------------------------------------
"""

#Draw Cells
drawCell(N, sqrPoint=[-2,-2], sqrSide=4)

#Draw Cross Field
drawCrossFieldFromAngle(arrAngleField, arrHasValue, sqrPoint=[-2,-2], sqrSide=4)

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()


"""
---------------------------------------------- Trace curves ----------------------------------------------
"""
