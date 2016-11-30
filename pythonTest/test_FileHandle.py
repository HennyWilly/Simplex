import os
import pytest
import env
from python.FileHandle import FileHandle


def test_shouldGetInputFiles():
    # This is a bad test, but I don't know how to test this function better...

    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, '..', 'input')
    fileHandle = FileHandle(path)
    files = fileHandle.getInputFiles()
    assert len(files) == 4


def test_shouldParseFile():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, '..', 'input', 'Exercise01.txt')
    lps = FileHandle.parseInputFile(path)

    # We don't need to check the lps here, because this is the job of "test_InputParser.py"
    assert len(lps) == 2


if __name__ == "__main__":
    pytest.main()
