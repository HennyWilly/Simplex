import time
import numpy as np

from python.Simplex import Simplex
from python.PivotElement import PivotElement
from python.LinearProblem import LinearProblem


class DualSimplex(Simplex):

    def __init__(self, linearProblem: LinearProblem):
        super().__init__(linearProblem)
        self.linearProblem.normalize()
        self.initTableau()

    def solve(self):
        self.printTableau()

        iterations = 0
        pivotElement = self.findPivotElement()
        
        while not pivotElement == None:
            iterations += 1
            print(pivotElement)
            self.calcElements(pivotElement)
            self.printTableau()
            pivotElement = self.findPivotElement()
            
        print('F(x_i) = {:.2f} (Iterations={:d})'.format(self.tableau[-1, -1], iterations))

        return self.tableau

    def initTableau(self):
        rows = len(self.linearProblem.additionalConditions) + 1
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        cols = numberOfCoeffs + len(self.linearProblem.additionalConditions) + 1
        self.tableau = np.zeros((rows, cols))
        self.tableau[-1, 0:numberOfCoeffs] = self.linearProblem.targetFunction.coeffs * (-1)
        self.tableau[-1, -1] = self.linearProblem.targetFunction.constant
        for i, additionalCondition in enumerate(self.linearProblem.additionalConditions):
            self.tableau[i, 0:numberOfCoeffs] = additionalCondition.coeffs
            self.tableau[i, numberOfCoeffs + i] = 1
            self.tableau[i, -1] = additionalCondition.rhs
        self.variables = np.array(range(numberOfCoeffs, cols-1))
        
    def checkAbort(self, pivotElement: PivotElement):
        pass

    def findPivotElement(self):
        numOfRows = len(self.linearProblem.additionalConditions)
        
        # abort if all b_i >= 0
        if len(np.where(self.tableau[0:numOfRows,-1] < 0)[0]) == 0:
            return None
                       
        row = np.argmin(self.tableau[0:numOfRows,-1])
        
        # abort if the pivot row contains only values >= 0
        if len(np.where(self.tableau[row, 0:-1] < 0)[0]) == 0:
            return None
            
        indices = np.where(self.tableau[row, 0:-1] < 0)
        values = self.tableau[-1, indices] / self.tableau[row, indices]
        idxMaxVal = np.argmax(values)
        col = indices[0][idxMaxVal]
        return PivotElement(row, col, self.tableau[row, col])
