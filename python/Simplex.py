import numpy as np
import time

from python.PivotElement import PivotElement
from python.LinearProblem import LinearProblem


class Simplex:
    def __init__(self, linearProblem: LinearProblem):
        self.linearProblem = linearProblem.normalize()
        self.tableau = None
        self.variables = None
        self.initTableau()
        self.printTableau()

    def solve(self):
        start = time.perf_counter()

        negative = True
        iterations = 0
        while negative is True:
            iterations += 1
            pivotElement = self.findPivotElement()
            print(pivotElement)
            self.calcElements(pivotElement)
            self.printTableau()
            negative = self.containsNegativeElements()
        print('F(x_i) = {:.2f} (Iterations={:d})'.format(self.tableau[-1, -1], iterations))

        # Generating result
        b = self.tableau[:-1, -1]
        x = np.zeros(self.tableau.shape[1] - 1)
        for resIdx, varIdx in enumerate(self.variables):
            x[varIdx] = b[resIdx]

        timeInSec = time.perf_counter() - start
        print("Execution time: {} ms".format(timeInSec * 1000))

        return x, self.tableau[-1, -1]

    def initTableau(self):
        rows = len(self.linearProblem.additionalConditions) + 1
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        cols = numberOfCoeffs + len(self.linearProblem.additionalConditions) + 1
        self.tableau = np.zeros((rows, cols))
        self.tableau[-1, 0:numberOfCoeffs] = self.linearProblem.targetFunction.coeffs * (-1)
        for i, additionalCondition in enumerate(self.linearProblem.additionalConditions):
            self.tableau[i, 0:numberOfCoeffs] = additionalCondition.coeffs
            self.tableau[i, numberOfCoeffs + i] = 1
            self.tableau[i, -1] = additionalCondition.rhs
        self.variables = np.array(range(numberOfCoeffs + 1, cols))

    def transformTableau(self):
        # TODO
        pass

    def printTableau(self):
        print('')
        for row in range(len(self.tableau)):
            row_str = ''
            for col in range(len(self.tableau[0])):
                if col == self.linearProblem.targetFunction.getNumberOfCoeffs():
                    row_str += '|'
                elif col == len(self.tableau[0]) - 1:
                    row_str += '|'
                row_str += '{:8.2f}\t'.format(self.tableau[row, col])
            print(row_str)

    def calcElements(self, pivot: PivotElement):
        pivotRow = pivot.row
        pivotCol = pivot.col
        self.variables[pivotRow] = pivotCol

        # calculate elements in pivot row
        self.tableau[pivotRow] = self.tableau[pivotRow] / self.tableau[pivotRow, pivotCol]
        # calculate elements except those that are in the pivot row or pivot column
        for row in range(len(self.tableau)):
            for col in range(len(self.tableau[0])):
                if row != pivotRow and col != pivotCol:
                    self.tableau[row, col] = self.tableau[row, col] - (
                        self.tableau[row, pivotCol] * self.tableau[pivotRow, col])
        # set elements to 0 except the pivot element
        for rowIndex in range(len(self.tableau)):
            if rowIndex != pivotRow:
                self.tableau[rowIndex, pivotCol] = 0

    def containsNegativeElements(self):
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        return True if len(np.where(self.tableau[-1, 0:numberOfCoeffs] < 0)[0]) > 0 else False

    def findPivotElement(self):
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        col = np.argmin(self.tableau[-1, 0:numberOfCoeffs])
        indices = np.where(self.tableau[:-1, col] > 0)
        values = self.tableau[indices, -1] / self.tableau[indices, col]
        idxMinVal = np.argmin(values)
        row = indices[0][idxMinVal]
        return PivotElement(row, col, self.tableau[row, col])
