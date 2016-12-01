import os
import time

import env
from python.PrimalSimplex import PrimalSimplex
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
                # linearProblem.plot()  # Uncomment this line to plot the LP
                primalSimplex = PrimalSimplex(linearProblem)
                if primalSimplex.isSolvable():
                    start = time.perf_counter()
                    primalSimplex.solve()
                    timeInSec = time.perf_counter() - start
                    print("Execution time: {} ms".format(timeInSec * 1000))
                else:
                    print('Can not solve LP with the primal simplex algorithm!')
                print('')


if __name__ == "__main__":
    main()
