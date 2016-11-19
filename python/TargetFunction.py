import re
import numpy as np

class TargetFunction:

    def __init__(self, equationStr: str):
        self.equationStr = equationStr.strip().replace(' ', '').replace('\n', '')
        self.numberOfCoeffs = 0
        self.coeffs = np.zeros(self.numberOfCoeffs)
        self.parseEquationStr()

    def parseEquationStr(self):
        self.parseNumberOfCoeffs()
        self.parseCoeffs()

    def parseNumberOfCoeffs(self):
        regexPattern = re.compile('F\(x[0-9]\.\.x[0-9]\)')
        match = regexPattern.match(self.equationStr)
        if match != None:
            regexPattern = re.compile('x[0-9]')
            matches = regexPattern.findall(match.group(0))
            self.numberOfCoeffs = int(matches[-1].replace('x', ''))
            self.coeffs = np.zeros(self.numberOfCoeffs)

    def parseCoeffs(self):
        regexPattern = re.compile('[-]*[0-9]*x\d*')
        splittedStr = self.equationStr.split('=')[-1]
        matches = regexPattern.findall(splittedStr)
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
