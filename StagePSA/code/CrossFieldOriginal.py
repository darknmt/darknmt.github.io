import numpy as np
from NURBS_Class import BSpline
import matplotlib.pyplot as plt
from NURBS import BSplineArray as NA
import random

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

def pmTextProcess(text):
    if text == '' or (text[0] != text[-1]):
        return ''
    return text[0]

def pmTextProcess_Stupid_Depricated(text):
    if text == '':
        return 0;
    N = len(text)
    tmp = text[0]
    res = 1 if tmp=='+' else -1
    for k in range(1,len(text)):
        if text[k] != tmp:
            tmp = text[k]
            res += 1 if tmp=='+' else -1
    return res


"""
---------------------------------------------- Drawing ----------------------------------------------
"""


def drawSurfaceArray(arrS):
        for i in range(arrS.shape[0]):
            plt.plot(arrS[i][:,0],arrS[i][:,1])

def lineUp(a,b, c='red', lw=0.5):
    plt.plot([a[0],b[0]], [a[1], b[1]], color=c, linewidth=lw)

def drawCross(pos, vect, side):
    a = vect*side*1.0/5
    b = np.array([-a[1],a[0]])
    lineUp((pos + a), (pos-a), 'red', lw=2)
    lineUp(pos +b, pos - b, 'green', lw=2)
    return

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

def markCell(i, j, N, sqrPoint=[0,0], sqrSide=1):
    plt.scatter((i+0.5)/N*sqrSide + sqrPoint[0], (j+0.5)/N*sqrSide + sqrPoint[1], marker='s', edgecolor='none',color='red')


"""
---------------------------------------------- Vector ----------------------------------------------
"""

def NormalizeField(arrField, arrHasValue):
    for i in range(arrField.shape[0]):
        for j in range(arrField.shape[1]):
            if arrHasValue[i,j]:
                arrField[i,j] = arrField[i,j]/(np.linalg.norm(arrField[i,j]))
    return

def posFromIndex(i, j, N, sqrPoint=[0,0], sqrSide=1):
    return np.array([(i+1)*1.0/N*sqrSide, (j+1)*1.0/N*sqrSide]) + np.array(sqrPoint)

#Input: x,y-position
#Output: i,j-position of cell
def cellFromPos(pos, N, sqrPoint=[0,0], sqrSide=1):
    return [(pos[0]-sqrPoint[0])//(sqrSide*1.0/N), (pos[1]-sqrPoint[1])//(sqrSide*1.0/N)]

def Horiz(a):
    if abs(a[0]) > abs(a[1]):
        return 1
    elif abs(a[0]) == abs(a[1]):
        return 0
    else:
        return -1
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

#draw trimming curve1
psing1 = np.array([0.3, -0.7])
psing2 = np.array([2, -2])
a = BSpline([0, 0, 0, 1, 1, 1], [psing1, [1.3, -0.7], [1.3, 0.3]])
b = BSpline([0, 0, 0, 1, 1, 1], [[1.3, 0.3], [1.3, 1.3], [0.3, 1.3]])
c = BSpline([0, 0, 0, 1, 1, 1], [[0.3, 1.3], [-0.7, 1.3], [-0.7, 0.3]])
d = BSpline([0, 0, 0, 1, 1, 1], [[-0.7, 0.3], [-0.7, -0.7], psing1])
trimCurve1 = a+b+c+d
trimCurve1.drawCurve(nPoint=800)

#draw trimming curve2
trimCurve2 = BSpline([0, 0, 0, 1, 2, 3, 3, 4, 5, 6,6, 7, 7, 7], [[1, -1.6], [1.5, -1.6], [1.5, -1], [1, -1], [1, -1.15], [1, -1], [0.5, -1], [0.5, -1.3], [0.8, -1.3], [0.5, -1.55], [1, -1.6]])
trimCurve2.drawCurve(nPoint=800)

#Draw Level Curve
#drawSurfaceArray(arrS)

N = 100
arrField = np.zeros([N, N, 2])
arrIndex = np.zeros([N-1, N-1])
arrHasValue = [[False for j in range(N)] for i in range(N)]
arrHasValue = np.array(arrHasValue)

"""-----------Curve1-----------"""
#Calculalte arrHasValue
data = trimCurve1.toArray(nPoint=800)
arrHasValue1 = np.array([[False for j in range(N)] for i in range(N)])
#Construct +/- array
arrMark =[['' for j in range(N)] for i in range(N)]
arrMark = np.array(arrMark)

for i in range(len(data)):
    c = cellFromPos(data[i], N, sqrPoint=[-2,-2], sqrSide=4)
    if data[(i+1)%len(data),0]-data[i,0] > 0:
        arrMark[c[0], c[1]] += '+'
    elif data[(i+1)%len(data),0]-data[i,0] < 0:
        arrMark[c[0], c[1]] += '-'

#Process +/- array
for i in range(N):
    turn=True
    for j in range(N):
        if arrMark[i,j] != '':
            arrHasValue1[i,j] = True
            arrMark[i,j] = pmTextProcess(arrMark[i,j])
            if j>0 and arrMark[i,j] != arrMark[i,j-1]:
                turn = not turn
        else:
            arrHasValue1[i,j] = turn

"""-----------Curve2-----------"""
#Calculalte arrHasValue
data = trimCurve2.toArray(nPoint=800)
arrHasValue2 = np.array([[False for j in range(N)] for i in range(N)])
#Construct +/- array
arrMark =[['' for j in range(N)] for i in range(N)]
arrMark = np.array(arrMark)

for i in range(len(data)):
    c = cellFromPos(data[i], N, sqrPoint=[-2,-2], sqrSide=4)
    if data[(i+1)%len(data),0]-data[i,0] > 0:
        arrMark[c[0], c[1]] += '+'
    elif data[(i+1)%len(data),0]-data[i,0] < 0:
        arrMark[c[0], c[1]] += '-'

#Process +/- array
for i in range(N):
    turn=True
    for j in range(N):
        if arrMark[i,j] != '':
            arrHasValue2[i,j] = True
            arrMark[i,j] = pmTextProcess(arrMark[i,j])
            if j>0 and arrMark[i,j] != arrMark[i,j-1]:
                turn = not turn
        else:
            arrHasValue2[i,j] = turn

for i in range(N):
    for j in range(N):
        arrHasValue[i,j] = arrHasValue1[i,j] and arrHasValue2[i,j]


#Test arrHasValue
for i in range(N):
    for j in range(N):
        if arrHasValue[i,j]:
            markCell(i, j, N, sqrPoint=[-2,-2], sqrSide=4)




#Inintiate Angle Field
#arrAngleField = VectorToAngle(arrField, arrHasValue)
"""
---------------------------------------------- Draw Vector Field ----------------------------------------------
"""

#Draw Cells
drawCell(N, sqrPoint=[-2,-2], sqrSide=4)

#Draw Cross Field
#drawCrossFieldFromAngle(arrAngleField, arrHasValue, sqrPoint=[-2,-2], sqrSide=4)

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
