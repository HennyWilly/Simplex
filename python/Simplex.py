from abc import ABCMeta, abstractmethod

from python.PivotElement import PivotElement
from python.LinearProblem import LinearProblem


class Simplex(metaclass=ABCMeta):

    def __init__(self, linearProblem: LinearProblem):
        self.linearProblem = linearProblem
        self.tableau = None
        self.variables = None

    @abstractmethod
    def solve(self):
        pass

    @abstractmethod
    def initTableau(self):
        pass

    @abstractmethod
    def checkAbort(self, pivotElement: PivotElement):
        pass

    @abstractmethod
    def findPivotElement(self):
        pass

    def calcElements(self, pivot: PivotElement):
        pivotRow = pivot.row
        pivotCol = pivot.col

        print('Switching x_{:d} with x_{:d}'.format(self.variables[pivotRow] + 1, pivotCol + 1))
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
