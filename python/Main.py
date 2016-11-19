import os
from Simplex import Simplex
from FileHandle import FileHandle

def main():
    fileHandle = FileHandle()
    inputFiles = fileHandle.getInputFiles()
    for file in inputFiles:
        if os.path.basename(file) == 'Exercise01.txt':  # TODO: remove this line
            linearProblems = fileHandle.parseInputFile(file)
            for linearProblem in linearProblems:
                print(linearProblem)
                simplex = Simplex(linearProblem)
                simplex.solve()
                print('')

if __name__ == "__main__":
    main()