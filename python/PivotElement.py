
class PivotElement:

    def __init__(self, row: int, col: int, value: float):
        if row < 0:
            raise ValueError("Invalid value of row: {:d}".format(row))
        if col < 0:
            raise ValueError("Invalid value of column: {:d}".format(col))

        self.row = row
        self.col = col
        self.value = value

    def __str__(self):
        return 'Pivot: row={:d}, col={:d}, value={:.2f}'.format(self.row, self.col, self.value)