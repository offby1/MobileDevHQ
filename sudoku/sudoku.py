import sys

# Terminology is from http://norvig.com/sudoku.html

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

    def other_row_coordinates(self, row_index, column_index):
        for r in set(range(0, len(self.rows))) - set([row_index]):
            yield r, column_index

    def other_column_coordinates(self, row_index, column_index):
        for c in set(range(0, len(self.rows[0]))) - set([column_index]):
            yield row_index, c

    def other_unit_coordinates(self, row_index, column_index):
        for r in range (3 * (row_index    // 3), 3 * (row_index    // 3 + 1)):
            for c in range (3 * (column_index // 3), 3 * (column_index // 3 + 1)):
                if r != row_index or c != column_index:
                    yield r, c

    def peer_coordinates(self, row_index, column_index):
        u = set(self.other_unit_coordinates(row_index, column_index))
        r = set(self.other_row_coordinates(row_index, column_index))
        c = set(self.other_column_coordinates(row_index, column_index))
        s = (u.union(r).union(c).difference(set([row_index, column_index])))

        return s

    def set_value(self, row_index, column_index, value):
        self.rows[row_index][column_index] = value

    def solve(self):
        for row_index, column_index in self.coordinates_of_holes():
            peer_values = [self.rows[r][c] for r,c in self.peer_coordinates(row_index, column_index)]
            print(row_index, column_index, sorted(set(peer_values)))
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
