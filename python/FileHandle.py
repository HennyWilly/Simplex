import glob
import os

from python.InputParser import parseLines


class FileHandle:
    def __init__(self, inputDir: str, outputDir: str = None, outputFileExtension: str = '.out'):
        self.inputDir = inputDir
        self.outputDir = outputDir if outputDir is not None else inputDir
        self.outputFileExtension = outputFileExtension

    def getInputFiles(self):
        path = os.path.join(self.inputDir, '*.txt')
        return glob.glob(path)

    # I think this method belongs into InputParser...
    @staticmethod
    def parseInputFile(file: str):
        with open(file) as inputFile:
            lines = inputFile.readlines()
        linearProblems = parseLines(lines)
        return linearProblems
