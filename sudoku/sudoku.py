import sys

class Board:
    def __init__(self, rows):
        self.rows = rows

    @classmethod
    def from_file(cls, inf):
        rows = []
        for line in inf:
            line = line.rstrip()
            rows.append(line.split(','))
        return cls(rows)

    def coordinates_of_holes(self):
        for r_index, row in enumerate(self.rows):
            for c_index, item in enumerate(row):
                if item == '-':
                    yield r_index, c_index

    def set_value(self, row_index, column_index, value):
        self.rows[row_index][column_index] = value

    def solve(self):
        for row_index, column_index in self.coordinates_of_holes():
            self.set_value(row_index, column_index, 'frotz!!')
        return self

    def __str__(self):
        return pprint.pformat(self.rows)

if __name__ == "__main__":
    import pprint
    b = Board.from_file(sys.stdin)
    holes = b.coordinates_of_holes()
    print("Board has {} holes".format(len(list(holes))))
    print(b)

    solution = b.solve()
    print(solution)
