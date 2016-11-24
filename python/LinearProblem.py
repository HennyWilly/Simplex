from Operator import Operator
from ProblemType import ProblemType
from TargetFunction import TargetFunction
from AdditionalCondition import AdditionalCondition

class LinearProblem:

    def __init__(self, description: str, problemType: ProblemType, targetFunction: TargetFunction, additionalConditions: [AdditionalCondition]):
        self.description = description.strip()
        self.problemType = problemType
        self.targetFunction = targetFunction
        self.additionalConditions = additionalConditions

    def normalize(self):
        additionalConditions = []
        for ac in self.additionalConditions:
            if ac.operator is Operator.Equals:
                ac1 = AdditionalCondition(ac.coeffs, Operator.SmallerThan, ac.rhs)
                ac2 = AdditionalCondition(ac.coeffs, Operator.GreaterThan, ac.rhs)
                additionalConditions.append(ac1, ac2)
            else:
                additionalConditions.append(ac)
        if self.problemType is ProblemType.Minimize:
            self.targetFunction.coeffs * (-1);
        return LinearProblem(self.description, ProblemType.Maximize, self.targetFunction, additionalConditions)

    def __str__(self):
        ret = '{:s}\n{:s} {:s}\n'.format(self.description, self.problemType, str(self.targetFunction))
        for ac in self.additionalConditions:
            ret += '{:s}\n'.format(str(ac))
        return ret
