from ProblemType import ProblemType
from TargetFunction import TargetFunction
from AdditionalCondition import AdditionalCondition

class LinearProblem:

    def __init__(self, description: str, problemType: ProblemType, targetFunction: TargetFunction, additionalConditions: [AdditionalCondition]):
        self.description = description.strip().replace('\n', '')
        self.problemType = problemType
        self.targetFunction = targetFunction
        self.additionalConditions = additionalConditions

    def __str__(self):
        ret = '{:s}\n{:s}\n'.format(self.description, self.targetFunction.equationStr)
        for additionalCondition in self.additionalConditions:
            ret += '{:s}\n'.format(additionalCondition.equationStr)
        return ret
