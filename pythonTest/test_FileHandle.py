import pytest

import env
from python.FileHandle import FileHandle


def test_shouldGetInputFiles():
    # This is a bad test, but I don't know how to test this function better...

    fileHandle = FileHandle("../input")
    files = fileHandle.getInputFiles()
    assert len(files) == 4


def test_shouldParseFile():
    file = "../input/Exercise01.txt"
    lps = FileHandle.parseInputFile(file)

    # We don't need to check the lps here, because this is the job of "test_InputParser.py"
    assert len(lps) == 2


if __name__ == "__main__":
    pytest.main()
