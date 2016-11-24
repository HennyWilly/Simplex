from ProblemType import ProblemType
from TargetFunction import TargetFunction
from AdditionalCondition import AdditionalCondition

class LinearProblem:

    def __init__(self, description: str, problemType: ProblemType, targetFunction: TargetFunction, additionalConditions: [AdditionalCondition]):
        self.description = description.strip()
        self.problemType = problemType
        self.targetFunction = targetFunction
        self.additionalConditions = additionalConditions

    def __str__(self):
        ret = '{:s}\n{:s} {:s}\n'.format(self.description, self.problemType, str(self.targetFunction))
        for additionalCondition in self.additionalConditions:
            ret += '{:s}\n'.format(str(additionalCondition))
        return ret
