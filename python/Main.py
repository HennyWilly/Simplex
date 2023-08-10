import os
import time

import env
from python.PrimalSimplex import PrimalSimplex
from python.DualSimplex import DualSimplex
from python.FileHandle import FileHandle


def main():
    currentDir = os.path.dirname(__file__)
    inputDir = os.path.join(currentDir, '..', 'input')
    fileHandle = FileHandle(inputDir)
    inputFiles = fileHandle.getInputFiles()
    for file in inputFiles:
        if os.path.basename(file) == 'Exercise14.txt':  # TODO: remove this line
            linearProblems = FileHandle.parseInputFile(file)
            for linearProblem in linearProblems:
                print(linearProblem)
                # linearProblem.plot()  # Uncomment this line to plot the LP
                primalSimplex = PrimalSimplex(linearProblem, None)
                start = time.perf_counter()
                if primalSimplex.isSolvable():
                    primalSimplex.solve()
                else:
                    print('Can not solve LP with the primal simplex algorithm!\nTry dual simplex algorithm:')
                    dualSimplex = DualSimplex(linearProblem)
                    tableau = dualSimplex.solve()
                    primalSimplex = PrimalSimplex(linearProblem, tableau)
                    if primalSimplex.isSolvable():
                        print('\nStart primal simplex algorithm:')
                        primalSimplex.solve()
                    else:
                        print('Still not solvable with primal algorithm')
                    
                timeInSec = time.perf_counter() - start
                print("Execution time: {} ms".format(timeInSec * 1000))
                print('')


if __name__ == "__main__":
    main()
