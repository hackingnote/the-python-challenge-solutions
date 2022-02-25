import time

class Seg:
    def __init__(self, length):
        self.length = length
        self.placements = []

    def __repr__(self):
        return '<Seg:len=' + str(self.length) + ',placements=' + str(self.placements) + '>'

class Bar:
    def __init__(self, axis, index, segs, length):
        self.segs = segs
        self.complete = False
        self.dirty = False
        self.axis = axis
        self.index = index
        self.length = length
        self.full_space = sum([seg.length for seg in self.segs]) + len(self.segs) - 1

    def is_full(self):
        return self.full_space == self.length

    def __repr__(self):
        return '<Bar:axis=' + str(self.axis) + ',index=' + str(self.index) + ',len=' + str(
            self.length) + ',full_space=' + str(
            self.full_space) + ',segs=' + str(self.segs) + ',dirty=' + str(self.dirty) + '>'

    def __lt__(self, other):
        return self.index - other.index

def load(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if (not line.startswith('#')) and len(line.strip()) != 0]
        raw = [list(map(int, line.split())) for line in lines]
        assert sum(raw[0]) == len(raw) - 1

        return raw[1:raw[0][0] + 1], raw[raw[0][0] + 1:]


def print_board(board):
    m = {1: '#', 0: ' ', None: '?'}
    print("\n".join([''.join([m[ele] for ele in row]) for row in board]))


def calc_space(segs):
    return sum([seg.length for seg in segs]) + len(segs) - 1


def calc_placement(bars):
    for bar in bars:
        for i in range(len(bar.segs)):
            seg = bar.segs[i]
            start = calc_space(bar.segs[:i]) + 1
            end = bar.length - calc_space(bar.segs[i + 1:]) - seg.length
            seg.placements = list(range(start, end))


def update_board(board, bar, i, value):
    if board[bar.axis][bar.index][i] == value:
        return False
    board[bar.axis][bar.index][i] = value
    board[1 - bar.axis][i][bar.index] = value
    return True


def mark_overlaps(board, bars):
    for bar in bars:
        for seg in bar.segs:
            for i in range(seg.placements[-1], seg.placements[0] + seg.length):
                if update_board(board, bar, i, 1):
                    bars[(1 - bar.axis) * h + i].dirty = True


def validate_placement(board, bar, iseg, placement):
    seg = bar.segs[iseg]

    # if the previous pixel is 1
    if placement > 0 and board[bar.axis][bar.index][placement - 1] == 1:
        return False

    # if any of the pixel inside the segment is 0
    elif 0 in board[bar.axis][bar.index][placement:placement + seg.length]:
        return False

    # if the next pixel is 1
    elif placement + seg.length < len(board[bar.axis][bar.index]) and board[bar.axis][bar.index][
                placement + seg.length] == 1:
        return False

    return True


def mark_flags(board, bar, tmp_placements, flags):
    prev = 0
    for i in range(len(tmp_placements)):
        seg = bar.segs[i]
        placement = tmp_placements[i]
        # print(seg, placement, placement + seg.length)
        for j in range(prev, placement):
            flags[j] |= 2
        for j in range(placement, placement + seg.length):
            flags[j] |= 1

        end = len(board[bar.axis][0])
        if i != len(tmp_placements) - 1:
            end = tmp_placements[i + 1]

        for j in range(placement + seg.length, end):
            flags[j] |= 2

        prev = placement + seg.length


# flag = 1: can be black,
# flag = 2: can be white,
# flag = 3: can be both
def check_bar(board, bar, start=0, iseg=0, tmp_placements=[], flags=[]):
    if iseg == len(bar.segs):
        last_seg = bar.segs[-1]
        if 1 in board[bar.axis][bar.index][tmp_placements[-1] + last_seg.length:]:
            return
        mark_flags(board, bar, tmp_placements, flags)
    else:
        seg = bar.segs[iseg]
        valid_placements = []
        for placement in seg.placements:
            # print(validate_placement(board, bar, iseg, placement))
            if validate_placement(board, bar, iseg, placement):
                valid_placements.append(placement)

        seg.placements = valid_placements

        for placement in seg.placements:
            if placement < start:
                continue

            if 1 in board[bar.axis][bar.index][start:placement]:
                continue

            tmp_placements[iseg] = placement
            check_bar(board, bar, start=placement + seg.length + 1, iseg=iseg + 1, tmp_placements=tmp_placements,
                      flags=flags)

if __name__ == '__main__':
    (hlens, vlens) = load("up.txt")

    h = len(hlens)
    v = len(vlens)

    bars = []

    for ind in range(len(hlens)):
        segs = [Seg(i) for i in hlens[ind]]
        bars.append(Bar(0, ind, segs, h))

    for ind in range(len(hlens)):
        segs = [Seg(i) for i in vlens[ind]]
        bars.append(Bar(1, ind, segs, h))

    board = [[[None] * v for i in range(h)], [[None] * v for i in range(h)]]

    calc_placement(bars)

    mark_overlaps(board, bars)

    while True:

        dirty_bars = [(sum([len(seg.placements) for seg in bar.segs]), bar) for bar in bars if bar.dirty]
        if len(dirty_bars) == 0:
            break
        effort, bar = min(dirty_bars)

        flags = [0] * len(board[bar.axis][0])

        print("Processing Bar: (" + str(bar.axis) + "," + str(bar.index) + ")")
        check_bar(board, bar, tmp_placements=[0] * len(bar.segs), flags=flags)

        for i in range(len(flags)):
            flag = flags[i]
            if flag == 1:
                if update_board(board, bar, i, 1):
                    bars[(1 - bar.axis) * h + i].dirty = True
            elif flag == 2:
                if update_board(board, bar, i, 0):
                    bars[(1 - bar.axis) * h + i].dirty = True
        bar.dirty = False

    print_board(board[0])

    print(time.process_time())
