data = """BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL"""

# with open("input.txt") as f:
#    data = f.read()
#    data = [line.strip() for line in data]


class FindSeat():
    def __init__(self, bpass):
        self.r = list(range(0, 128))
        self.c = list(range(0, 8))
        self.row = [c for c in bpass[:7]]
        self.col = [c for c in bpass[7:]]
        self.row_num = self.find_seat(self.row)
        self.col_num = self.find_seat(self.col)
        # self.seat_num = self.row_num * 8 + self.col_num

    def find_seat(self, lst):
        if len(lst) == 7:
            return self.split(self.r, lst)
        else:
            return self.split(self.c, lst)

    def split(self, lst, data):
        lst = self.upper(lst) if data.pop(0) == 'F' else self.lower(lst)
        if len(lst) > 1:
            self.split(lst, data)
        else:
            print(lst[0])
            return lst[0]

    def upper(self, lst):
        return lst[:len(lst)//2]

    def lower(self, lst):
        return lst[len(lst)//2:]


seat = FindSeat('BFFFBBFRRR')
print(seat.row_num)
