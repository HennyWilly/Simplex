import os
import glob
from ProblemType import ProblemType
from LinearProblem import LinearProblem
from TargetFunction import TargetFunction
from AdditionalCondition import AdditionalCondition

class FileHandle:

    def __init__(self, inputDirName: str='input', outputDirName: str='output', outputFileExtension: str='.out'):
        self.inputDirName = inputDirName
        self.outputDirName = outputDirName
        self.outputFileExtension = outputFileExtension
        self.workingDir = os.path.dirname(__file__)

    def getInputFiles(self):
        path = os.path.join(self.workingDir, '..', self.inputDirName, '*')
        return glob.glob(path)

    def parseInputFile(self, file: str):
        linearProblems = []
        with open(file) as inputFile:
            lines = inputFile.readlines()
            indices = [lines.index(line) for line in lines if (not line.startswith('#') and (str(ProblemType.Minimize) in line or str(ProblemType.Maximize) in line))]
            for idx in indices:
                currentLine = lines[idx]
                description = lines[idx - 1]
                targetFunction = TargetFunction(currentLine[4:])
                numberOfCoeffs = targetFunction.numberOfCoeffs
                problemType = ProblemType.Maximize if str(ProblemType.Maximize) in currentLine else ProblemType.Minimize
                additionalConditions = []
                j = 1
                line = lines[idx + 1]
                while line not in ['\n', '\r\n']:
                    additionalConditions.append(AdditionalCondition(line, numberOfCoeffs))
                    j += 1
                    if idx+j < len(lines):
                        line = lines[idx + j]
                    else:
                        break
                if len(additionalConditions) > 0:
                    linearProblems.append(LinearProblem(description, problemType, targetFunction, additionalConditions))
        return linearProblems
