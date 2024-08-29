
import math

def multiplymatrix(A,B):
    
    if len(A[0]) == len(B):
        C = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    C[i][j] += A[i][k] * B[k][j]

        return C
    else:
        return None

def multiplyMatrixVector(A,B):
    # A es el vector
    # B es la matriz
    if len(A) == len(B):
        C = [0,0,0,0]

        for i in range(len(A)):
            for j in range(len(B[0])):
                C[i] += B[i][j] * A[j]

        return C
    else:
        return None
    

def barycentrinCoords(A,B,C,P):

    areaPBC = (B[1]- C[1]) * (P[0]-C[0]) + (C[0] - B[0]) * (P[1]-C[1])
    areaACP = (C[1]- A[1]) * (P[0]-C[0]) + (A[0] - C[0]) * (P[1]-C[1])
    areaABC = (B[1]- C[1]) * (A[0]-C[0]) + (C[0] - B[0]) * (A[1]-C[1])


    if areaABC ==0:
        return None

    u = areaPBC / areaABC
    v = areaACP / areaABC
    w = 1-u-v

    if 0<=u<=1 and 0<=v<=1 and 0<=w<=1 and math.isclose(u+v+w,1.0):
        return u,v,w
    else:
        return None

def getMatrixMinor(matrix,i,j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])] #minor matrix

def matrixDeterm(matrix):
    if len(matrix) == 2: #case for 2x2 matrix
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1)**c)*matrix[0][c]*matrixDeterm(getMatrixMinor(matrix,0,c))
    return determinant

def invMatrix(mx):
    det = matrixDeterm(mx)
    if(det==0):
        print('Determinant is zero')
        return
    if len(mx) == 2: #case for 2x2 matrix 
        return [[mx[1][1]/det, -1*mx[0][1]/det],
                [-1*mx[1][0]/det, mx[0][0]/det]]
    cofactors = []
    for i in range(len(mx)):
        cofactRow = []
        for j in range(len(mx)):
            minorValue = getMatrixMinor(mx,i,j)
            cofactRow.append(((-1)**(i+j)) * matrixDeterm(minorValue))
        cofactors.append(cofactRow)
        
    inverse = list(map(list,zip(*cofactors))) #gets the transpose of the matrix
    for i in range(len(inverse)):
        for j in range(len(inverse)):
            inverse[i][j] = inverse[i][j]/det
    return inverse

def substractionVectors(a,b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def prodCrossV(a,b):
    cross_product = [a[1] * b[2] - a[2] * b[1],
                     a[2] * b[0] - a[0] * b[2],
                     a[0] * b[1] - a[1] * b[0]]
    return cross_product

def normalizeVector(vector):
    vectorList = list(vector)
    magnitude = math.sqrt(sum(e ** 2 for e in vectorList))
    if magnitude == 0: #error if magnitude is 0
        print("Unable to normalize")
    
    normVector = [e / magnitude for e in vectorList]
    return tuple(normVector)
     
def dotProd(v1, v2):
    return sum(x*y for x, y in zip(v1, v2))

