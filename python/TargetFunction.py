import numpy as np


class TargetFunction:
    def __init__(self, coeffs: np.array, constant: int=0):
        self.coeffs = np.array(coeffs)
        self.constant = constant

    def getNumberOfCoeffs(self):
        return len(self.coeffs)

    def changeSign(self):
        self.coeffs *= -1
        self.constant *= -1

    def __str__(self):
        ret = 'F(x{:d}..x{:d}) = '.format(1, self.getNumberOfCoeffs())
        for i, val in enumerate(self.coeffs):
            valInt = int(val)
            if i > 0 and valInt >= 0:
                ret += '+ '
            ret += '{:d}x{:d} '.format(valInt, i + 1)
        if self.constant > 0:
            ret += '+ {:d}'.format(self.constant)
        elif self.constant < 0:
            ret += '- {:d}'.format(self.constant*(-1))
        return ret
