import time
import numpy as np

from python.Simplex import Simplex
from python.PivotElement import PivotElement
from python.LinearProblem import LinearProblem


class DualSimplex(Simplex):

    def __init__(self, linearProblem: LinearProblem):
        super().__init__(linearProblem)
        self.initTableau()
        self.printTableau()

    def solve(self):
        # TODO: implement
        pass

    def initTableau(self):
        # TODO: implement
        pass

    def checkAbort(self, pivotElement: PivotElement):
        # TODO: implement
        # abort if all b_i >= 0
        # abort if the pivot row contains only values >= 0
        pass

    def findPivotElement(self):
        # TODO: implement
        pass
