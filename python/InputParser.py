import re
import numpy as np

try:
    from .Operator import Operator
    from .ProblemType import ProblemType
    from .LinearProblem import LinearProblem
    from .TargetFunction import TargetFunction
    from .AdditionalCondition import AdditionalCondition
except SystemError:
    from Operator import Operator
    from ProblemType import ProblemType
    from LinearProblem import LinearProblem
    from TargetFunction import TargetFunction
    from AdditionalCondition import AdditionalCondition


def parseLines(lines: [str]):
    linearProblems = []
    lines = [line.strip() for line in lines]
    indices = [lines.index(line) for line in lines if
               (not line.startswith('#') and (str(ProblemType.Minimize) in line or str(ProblemType.Maximize) in line))]
    for idx in indices:
        currentLine = lines[idx]
        description = lines[idx - 1].strip().replace('\n', '')
        targetFunction = parseTargetFunctionStr(currentLine[4:])
        numberOfCoeffs = targetFunction.getNumberOfCoeffs()
        problemType = ProblemType.Maximize if str(ProblemType.Maximize) in currentLine else ProblemType.Minimize
        additionalConditions = []
        j = 1
        line = lines[idx + 1]

        # TODO Check if we already reached the next index
        while line not in ['\n', '\r\n', '']:
            additionalCondition = parseAdditionalConditionStr(line, numberOfCoeffs)
            additionalConditions.append(additionalCondition)
            j += 1
            if idx + j < len(lines):
                line = lines[idx + j]
            else:
                break
        if len(additionalConditions) > 0:
            lp = LinearProblem(description, problemType, targetFunction, additionalConditions)
            linearProblems.append(lp)
    return linearProblems


def parseAdditionalConditionStr(additionalConditionStr: str, numberOfCoeffs: int):
    additionalConditionStr = additionalConditionStr.strip().replace(' ', '').replace('\n', '')
    coeffs = parseCoeffs(additionalConditionStr, numberOfCoeffs)
    operator = parseOperator(additionalConditionStr)
    rhs = parseRhs(additionalConditionStr, operator)
    return AdditionalCondition(coeffs, operator, rhs)


def parseTargetFunctionStr(targetFunctionStr: str):
    targetFunctionStr = targetFunctionStr.strip().replace(' ', '').replace('\n', '')
    numberOfCoeffs = parseNumberOfCoeffs(targetFunctionStr)
    splittedStr = targetFunctionStr.split('=')[-1]
    coeffs = parseCoeffs(splittedStr, numberOfCoeffs)
    return TargetFunction(coeffs)


def parseCoeffs(equationStr: str, numberOfCoeffs):
    coeffs = np.zeros(numberOfCoeffs)
    regexPattern = re.compile('[-]*\d*x\d*')
    matches = regexPattern.findall(equationStr)
    for match in matches:
        splitArray = match.split('x')
        if splitArray[0] is '':
            val = 1
        elif splitArray[0] is '-':
            val = -1
        else:
            val = int(splitArray[0])
        idx = int(splitArray[1]) - 1
        if 0 <= idx < numberOfCoeffs:
            coeffs[idx] = val
    return coeffs


def parseNumberOfCoeffs(equationStr: str):
    numberOfCoeffs = 0
    regexPattern = re.compile('F\(x\d\.\.x\d\)')
    match = regexPattern.match(equationStr)
    if match != None:
        regexPattern = re.compile('x\d')
        matches = regexPattern.findall(match.group(0))

        lowerBound = int(matches[0].replace('x', ''))
        upperBound = int(matches[1].replace('x', ''))

        if lowerBound > upperBound:
            raise ValueError("Lower bound {} is bigger than upper bound {}".format(lowerBound, upperBound))

        numberOfCoeffs = upperBound - lowerBound + 1
    return numberOfCoeffs


def parseOperator(equationStr: str):
    operator = Operator.Unknown
    if equationStr.find('<=') > -1:
        operator = Operator.SmallerThan
    elif equationStr.find('>=') > -1:
        operator = Operator.GreaterThan
    elif equationStr.find('<') > -1:
        operator = Operator.Smaller
    elif equationStr.find('>') > -1:
        operator = Operator.Greater
    elif equationStr.find('=') > -1:
        operator = Operator.Equals
    return operator


def parseRhs(equationStr: str, operator: Operator):
    result = 0
    if operator is not Operator.Unknown:
        splitArray = equationStr.split(str(operator))
        result = int(splitArray[-1])
    return result
