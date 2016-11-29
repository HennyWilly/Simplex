import os

import env
from python.Simplex import Simplex
from python.FileHandle import FileHandle


def main():
    currentDir = os.path.dirname(__file__)
    inputDir = os.path.join(currentDir, '..', 'input')
    fileHandle = FileHandle(inputDir)
    inputFiles = fileHandle.getInputFiles()
    for file in inputFiles:
        if os.path.basename(file) == 'Exercise01.txt':  # TODO: remove this line
            linearProblems = FileHandle.parseInputFile(file)
            for linearProblem in linearProblems:
                print(linearProblem)
                simplex = Simplex(linearProblem)
                simplex.solve()
                print('')


if __name__ == "__main__":
    main()
