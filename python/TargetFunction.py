import numpy as np


class TargetFunction:
    def __init__(self, coeffs: np.array):
        self.coeffs = np.array(coeffs)

    def getNumberOfCoeffs(self):
        return len(self.coeffs)

    def __str__(self):
        ret = 'F(x{:d}..x{:d}) = '.format(1, self.getNumberOfCoeffs())
        for i, val in enumerate(self.coeffs):
            valInt = int(val)
            if i > 0 and valInt >= 0:
                ret += '+ '
            ret += '{:d}x{:d} '.format(valInt, i + 1)
        return ret
