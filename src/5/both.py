with open("input.txt") as f:
    data = f.readlines()


class FindSeat:
    def __init__(self, bpass):
        self.r = list(range(0, 128))
        self.c = list(range(0, 8))
        self.row = [c for c in bpass[:7]]
        self.col = [c for c in bpass[7:]]
        self.row_num = self.find_seat(self.row)
        self.col_num = self.find_seat(self.col)
        self.seat_num = self.row_num * 8 + self.col_num

    def find_seat(self, lst):
        if len(lst) == 7:
            return self.split(self.r, lst)
        else:
            return self.split(self.c, lst)

    def split(self, lst, data):
        lst = (
            self.upper(lst)
            if data[0] == "F" or data[0] == "L"
            else self.lower(lst)
        )
        if len(lst) > 1:
            data.pop(0)
            return self.split(lst, data)

        return lst[0]

    def upper(self, lst):
        return lst[: len(lst) // 2]

    def lower(self, lst):
        return lst[len(lst) // 2:]


def find_highest_seat():
    highest = -1
    for entry in data:
        seat_num = FindSeat(entry).seat_num
        if seat_num > highest:
            highest = seat_num
    return highest


def find_own_seat():
    # Hacky
    all_seats = []
    for entry in data:
        all_seats.append(FindSeat(entry).seat_num)
    all_seats = set(sorted(all_seats))
    possible_seats = set(range(0, 981))
    for seat in possible_seats:
        if seat not in all_seats:
            print(seat)
