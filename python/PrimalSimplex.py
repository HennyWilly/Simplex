import numpy as np

from python.Simplex import Simplex
from python.PivotElement import PivotElement
from python.LinearProblem import LinearProblem


class PrimalSimplex(Simplex):

    def __init__(self, linearProblem: LinearProblem):
        super().__init__(linearProblem.normalize())
        self.initTableau()

    def solve(self):
        self.printTableau()

        iterations = 0
        pivotElement = None
        while not self.checkAbort(pivotElement):
            iterations += 1
            pivotElement = self.findPivotElement()
            print(pivotElement)
            self.calcElements(pivotElement)
            self.printTableau()
        print('F(x_i) = {:.2f} (Iterations={:d})'.format(self.tableau[-1, -1], iterations))

        # Generating result
        x = self.getResult()

        return x, self.tableau[-1, -1]

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
        self.variables = np.array(range(numberOfCoeffs + 1, cols))

    def checkAbort(self, pivotElement: PivotElement):
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        # abort if the F line contains only positive values (>= 0)
        abort = False if len(np.where(self.tableau[-1, 0:numberOfCoeffs] < 0)[0]) > 0 else True
        # abort if the pivot column contains only values <= 0
        if not abort and pivotElement is not None:
            abort = False if len(np.where(self.tableau[:, pivotElement.col] > 0)[0]) > 0 else True
        return abort

    def findPivotElement(self):
        numberOfCoeffs = self.linearProblem.targetFunction.getNumberOfCoeffs()
        col = np.argmin(self.tableau[-1, 0:numberOfCoeffs])
        indices = np.where(self.tableau[:-1, col] > 0)
        values = self.tableau[indices, -1] / self.tableau[indices, col]
        idxMinVal = np.argmin(values)
        row = indices[0][idxMinVal]
        return PivotElement(row, col, self.tableau[row, col])

    def isSolvable(self):
        # The LP can not be solved if there is at least one b_i < 0
        return False if len(np.where(self.tableau[:, -1] < 0)[0]) > 0 else True

    def getResult(self):
        b = self.tableau[:-1, -1]
        x = np.zeros(self.tableau.shape[1] - 1)
        for resIdx, varIdx in enumerate(self.variables):
            x[varIdx] = b[resIdx]
        return x
