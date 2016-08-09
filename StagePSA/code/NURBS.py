""" Basic NURBS Manipulation

This module implement certain base functions of isogeometric analysis, including the B-Splines given the knot vector and base points,
or the NURBS given the weight vector in addition.

See also:
    A comprehensive reference can be found in the book of Thomas J.R. Hughes.

"""


import numpy as np

def BSpline(knot, i, p, x): #i from 1 to len(knot) - p - 1
    """Function generating B-Spline function by recurrence.

    Args:
        knot (array): knot vector.
        i (int): order of B-Spline
        p (int): polynomial degree.
        x (float): position in parametric domain.

    Returns:
        (float): value of the i-th B-Spline function of degree p at point x.

    """
    if p == 0:
            if (knot[i] <= x) and ((x < knot[i+1]) or (x == knot[i+1] and knot[i+1] == knot[-1])):
                    return 1
            else:
                return 0
    else:
        res = 0
        if knot[i+p] != knot[i]:
            res += (x - knot[i]) /(knot[i+p] - knot[i])*BSpline(knot, i, p - 1, x)
        if knot[i+p+1] != knot[i+1]:
            res += (knot[i+p+1] - x) /(knot[i+p+1] - knot[i+1])*BSpline(knot, i + 1, p - 1, x)
        return res

# Input: [-1] + knot
# Output: [-1] + N[i]
def BSplineArray(knot, p, x): #return BSpline[i] for i from 1 to len(knot) - p - 2 since knot = [-1] + real_knot
    """Function generating B-Spline functions by array recurrence.
    This function calculates all B-Spline of degree p, thus has better running time.

    Note:
        To facilitate the implementation, we add [-1] to the beginning of knot vector and the return vector.
        For example, one should call the function with knot = [-1,0,1,2] if one want the knot vector to be [0,1,2]

    Args:
        knot (int array): knot vector.
        p (int): polynomial degree.
        x (float): position in parametric domain.

    Returns:
        (float array): value of the all i-th B-Splines of degree p at point x.

    """
    res = [-1]
    if p == 0:
        for i in range(1,len(knot)-1 - p):
            if (knot[i] <= x) and ((x < knot[i+1]) or (x == knot[i+1] and knot[i+1] == knot[-1])):
                res += [1]
            else:
                res += [0]
        return res
    else:
        Bp = BSplineArray(knot, p-1, x)
        for i in range(1, len(knot) - p - 1):
            resi = 0
            if knot[i+p] != knot[i]:
                resi += (x - knot[i]) / (knot[i+p] - knot[i])*Bp[i]
            if knot[i+p+1] != knot[i+1]:
                resi += (knot[i+p+1] - x) / (knot[i+p+1] - knot[i+1])*Bp[i+1]
            res += [resi]
        return res

# Input: [-1] + knot, w normal length
# Output: R[i]
def NURBSArray(knot, w, p, x):
    """Function generating NURBS functions by array recurrence.
    This function calculates all NURBS of degree p.

    Note:
        To facilitate the implementation, we add [-1] to the beginning of knot vector.
        For example, one should call the function with knot = [-1,0,1,2] if one want the knot vector to be [0,1,2]

    Args:
        knot (int array): knot vector.
        w (float array): weight vector.
        p (int): polynomial degree.
        x (float): position in parametric domain.

    Returns:
        (float array): value of the all i-th B-Splines of degree p at point x.

    """
    BSA = np.array(BSplineArray(knot, p, x))
    BSA = map(float,BSA[1:len(BSA)])
    bigW = np.array(w)*np.array(BSA)
    bigW = bigW/sum(bigW)
    return bigW
