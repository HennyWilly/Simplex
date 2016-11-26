from enum import Enum


class ProblemType(Enum):
    Minimize = 'min.'
    Maximize = 'max.'

    def __str__(self):
        return '{:s}'.format(self.value)
