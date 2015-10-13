import sys

class Board:
    def __init__(self, cell_array):
        self.cells = cell_array

    @classmethod
    def from_file(cls, inf):
        cell_array = []
        for line in inf:
            line = line.rstrip()
            cells = line.split(',')
            cell_array.append(cells)
        return cls(cell_array)

    def solve(self):
        return self

if __name__ == "__main__":
    import pprint
    b = Board.from_file(sys.stdin)
    pprint.pprint(b)
    solution = b.solve()
    pprint.pprint(solution)
