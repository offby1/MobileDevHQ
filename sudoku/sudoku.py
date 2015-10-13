import sys

def read_board(inf):
    board = []
    for line in inf:
        line = line.rstrip()
        cells = line.split(',')
        board.append(cells)
    return board

if __name__ == "__main__":
    import pprint
    pprint.pprint(read_board(sys.stdin))
