from enum import Enum


class Operator(Enum):
    Unknown = '<Operator.Unknown>'
    Smaller = '<'
    SmallerThan = '<='
    Greater = '>'
    GreaterThan = '>='
    Equals = '='

    def __str__(self):
        return '{:s}'.format(self.value)
