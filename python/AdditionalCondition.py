import numpy as np

from python.Operator import Operator


class AdditionalCondition:
    def __init__(self, coeffs: np.array, operator: Operator, rhs: int):
        self.coeffs = np.array(coeffs)
        self.operator = operator
        self.rhs = rhs

    def getNumberOfCoeffs(self):
        return len(self.coeffs)

    def isValidSolution(self, solution: np.array):
        solution = np.array(solution)
        isValid = False
        lhs = np.sum(self.coeffs * solution)
        if self.operator is Operator.Smaller:
            isValid = (lhs < self.rhs)
        elif self.operator is Operator.SmallerThan:
            isValid = (lhs <= self.rhs)
        elif self.operator is Operator.Greater:
            isValid = (lhs > self.rhs)
        elif self.operator is Operator.GreaterThan:
            isValid = (lhs >= self.rhs)
        elif self.operator is Operator.Equals:
            isValid = (lhs == self.rhs)
        return isValid

    def __str__(self):
        ret = ''
        for i, val in enumerate(self.coeffs):
            valInt = int(val)
            if i > 0 and valInt >= 0:
                ret += '+ '
            ret += '{:d}x{:d} '.format(valInt, i + 1)
        ret += '{:s} {:d}'.format(self.operator, self.rhs)
        return ret
