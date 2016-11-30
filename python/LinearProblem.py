import numpy as np

from python.Operator import Operator
from python.ProblemType import ProblemType
from python.TargetFunction import TargetFunction
from python.AdditionalCondition import AdditionalCondition


class LinearProblem:
    def __init__(self, description: str, problemType: ProblemType, targetFunction: TargetFunction,
                 additionalConditions: [AdditionalCondition]):
        self.description = description.strip()
        self.problemType = problemType
        self.targetFunction = targetFunction
        self.additionalConditions = additionalConditions

    def normalize(self):
        targetFunctionCoeffs = self.targetFunction.coeffs
        additionalConditions = []
        for ac in self.additionalConditions:
            if ac.operator is Operator.Equals:
                ac1 = AdditionalCondition(ac.coeffs, Operator.SmallerThan, ac.rhs)
                ac2 = AdditionalCondition(-1 * ac.coeffs, Operator.SmallerThan, -1 * ac.rhs)
                additionalConditions.append(ac1)
                additionalConditions.append(ac2)
            elif ac.operator is Operator.GreaterThan:
                additionalConditions.append(AdditionalCondition(-1 * ac.coeffs, Operator.SmallerThan, -1 * ac.rhs))
            else:
                additionalConditions.append(ac)
        if self.problemType is ProblemType.Minimize:
            targetFunctionCoeffs *= -1
        return LinearProblem(self.description, ProblemType.Maximize, TargetFunction(targetFunctionCoeffs),
                             additionalConditions)

    def isValidSolution(self, solution: np.array):
        isValid = False
        if len(solution) == len(self.targetFunction.getNumberOfCoeffs()):
            for additionalCondition in self.additionalConditions:
                isValid = additionalCondition.isValidSolution(solution)
                if not isValid:
                    break
        return isValid

    def __str__(self):
        ret = '{:s}\n{:s} {:s}\n'.format(self.description, self.problemType, str(self.targetFunction))
        for ac in self.additionalConditions:
            ret += '{:s}\n'.format(str(ac))
        return ret
