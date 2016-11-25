import numpy as np

try:
    from .Operator import Operator
except SystemError:
    from Operator import Operator

class AdditionalCondition:

    def __init__(self, coeffs: np.array, operator: Operator, rhs: int):
        self.coeffs = coeffs
        self.operator = operator
        self.rhs = rhs

    def getNumberOfCoeffs(self):
        return len(self.coeffs)

    def __str__(self):
        ret = ''
        for i, val in enumerate(self.coeffs):
            valInt = int(val)
            if i > 0 and valInt >= 0:
                    ret += '+ '
            ret += '{:d}x{:d} '.format(valInt, i + 1)
        ret += '{:s} {:d}'.format(self.operator, self.rhs)
        return ret
