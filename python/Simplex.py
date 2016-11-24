import numpy as np
from ProblemType import ProblemType
from PivotElement import PivotElement
from LinearProblem import LinearProblem

class Simplex:

    def __init__(self, linearProblem: LinearProblem):
        self.linearProblem = linearProblem
        self.tableau = None
        self.initTableau()
        self.printTableau()

    def solve(self):
        if self.linearProblem.problemType is ProblemType.Minimize:
            self.transformTableau()
        negative = True
        iterations = 0
        while negative is True:
            iterations += 1
            pivotElement = self.findPivotElement()
            print(pivotElement)
            self.calcElements(pivotElement.row, pivotElement.col)
            self.printTableau()
            negative = self.containsNegativeElements()
        print('F(x_i) = {:.2f} (Iterations={:d})'.format(self.tableau[-1, -1], iterations))

    def initTableau(self):
        rows = len(self.linearProblem.additionalConditions) + 1
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        cols = numberOfCoeffs + len(self.linearProblem.additionalConditions) + 1
        self.tableau = np.zeros((rows, cols))
        self.tableau[-1, 0:numberOfCoeffs] = self.linearProblem.targetFunction.coeffs * (-1)
        for i, additionalCondition in enumerate(self.linearProblem.additionalConditions):
            self.tableau[i, 0:numberOfCoeffs] = additionalCondition.coeffs
            self.tableau[i, numberOfCoeffs+i] = 1
            self.tableau[i, -1] = additionalCondition.rhs

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
                elif col == len(self.tableau[0])-1:
                    row_str += '|'
                row_str += '{:8.2f}\t'.format(self.tableau[row, col])
            print(row_str)

    def calcElements(self, pivotRow: int, pivotCol: int):
        # calculate elements in pivot row
        self.tableau[pivotRow] / self.tableau[pivotRow, pivotCol]
        # calculate elements except those that are in the pivot row or pivot column
        for row in range(len(self.tableau)):
            for col in range(len(self.tableau[0])):
                if row != pivotRow and col != pivotCol:
                    self.tableau[row, col] = self.tableau[row, col] - (self.tableau[row, pivotCol]*self.tableau[pivotRow, col])
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
        row = np.argmin(self.tableau[indices, -1] / self.tableau[indices, col])
        return PivotElement(row, col, self.tableau[row, col])
