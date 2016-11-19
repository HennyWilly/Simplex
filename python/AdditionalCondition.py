import re
import numpy as np
from Operator import Operator

class AdditionalCondition:

    def __init__(self, equationStr: str, numberOfCoeffs: int):
        self.equationStr = equationStr.strip().replace(' ', '').replace('\n', '')
        self.numberOfCoeffs = numberOfCoeffs
        self.coeffs = np.zeros(numberOfCoeffs)
        self.operator = Operator.Unknown
        self.result = 0
        self.parseEquationStr()

    def parseEquationStr(self):
        self.parseCoeffs()
        self.parseOperator()
        self.parseRhs()

    def parseCoeffs(self):
        regexPattern = re.compile('[-]*[0-9]*x\d*')
        matches = regexPattern.findall(self.equationStr)
        for match in matches:
            splitArray = match.split('x')
            if splitArray[0] is '':
                val = 1
            elif splitArray[0] is '-':
                val = -1
            else:
                val = int(splitArray[0])
            idx = int(splitArray[1]) - 1
            if 0 <= idx < self.numberOfCoeffs:
                self.coeffs[idx] = val

    def parseOperator(self):
        if self.equationStr.find('<=') > -1:
            self.operator = Operator.SmallerThan
        elif self.equationStr.find('>=') > -1:
            self.operator = Operator.GreaterThan
        elif self.equationStr.find('<') > -1:
            self.operator = Operator.Smaller
        elif self.equationStr.find('>') > -1:
            self.operator = Operator.Greater
        elif self.equationStr.find('=') > -1:
            self.operator = Operator.Equals

    def parseRhs(self):
        if self.operator is not Operator.Unknown:
            splitArray = self.equationStr.split(str(self.operator))
            self.result = int(splitArray[-1])
