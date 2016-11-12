import numpy as np

def simplex(A, b, f):
    def checkInput(A, b, f):
        if(A.shape[0] != len(b)):
            raise ValueError("Dimensions of A and b do not match: #rows(A)={}, #rows(b)={}".format(A.shape[0], len(b)))
        if(A.shape[1] != len(f)):
            raise ValueError("Dimensions of A and f do not match: #cols(A)={}, #cols(f)={}".format(A.shape[1], len(f)))
        
        for i, bi in enumerate(b):
            if(bi < 0):
               raise ValueError("b contains a negative value {} at index {}".format(bi, i))
    
    def isValidSolution(A, b, f):
        raise NotImplementedError("")
    
    def getPossiblePivotCols(f):
        indices = np.array([])
        for index, value in enumerate(f):
            if(value >= 0):
                continue
            indices = np.append(indices, index)
        if indices.size > 0:
            # List not empty
            indices = indices.astype(int)
        return indices
    
    def getPivotElementPosition(A, b, f):
        possibleCols = getPossiblePivotCols(f)
        if (possibleCols.size == 0):
            col, row = -1, -1
        else:
            col = getBestPivotCol(A, b, f, possibleCols)
            row = getPivotRow(A, b, col)
        return row, col
    
    def getBestPivotCol(A, b, f, possiblePivotCols):
        smalestFIndex = np.argsort(f)[0]
        if (not smalestFIndex in possiblePivotCols):
            raise AssertionError("This should never happen: Best pivot index is not in possibleCols-Array")
        
        #print "Best pivot column index: {}".format(np.argsort(f)[0])
        return np.argsort(f)[0]
    
    def getPivotRow(A, b, pivotCol):
        bestIdx = -1
        bestQuot = -1
        
        for i, bi in enumerate(b):
            Aij = A[i, pivotCol]
            if (Aij <= 0):
                continue
            quot = bi / Aij
            if (bestIdx == -1 or bestQuot > quot):
                bestIdx = i
                bestQuot = quot
        
        return bestIdx
    
    A = np.array(A).astype(np.float32, copy=False)
    b = np.array(b).flatten().astype(np.float32, copy=False)
    f = np.array(f).flatten().astype(np.float32, copy=False)
    res = 0
    
    checkInput(A, b, f)
    
    while(True):
        #print "{}".format(A)
        #print "b = {}".format(b)
        #print "f = {}".format(f)
        #print "res = {}".format(res)
        
        (row, col) = getPivotElementPosition(A, b, f)
        if (col == -1 or row == -1):
            break
        
        #print row, col
        
        for i in range(len(b)):
            if (i == row):
                b[row] = b[row] / A[row, col]
                A[row, :] = A[row, :] / A[row, col]
            else:
                faktor = A[i, col] / A[row, col]
                #print "Faktor({}) = {}/{} = {}".format(i, A[i, col], A[row, col], faktor)
                b[i] = b[i] - faktor * b[row]
                A[i, :] = A[i, :] - faktor * A[row, :]
        
        faktor = f[col] / A[row, col]
        f = f - faktor * A[row, :]
        res = res - faktor * b[row]
        #print "---------------------------------------------------------"
    
    return (A, b, f, res)