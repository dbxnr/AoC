import re

from collections import deque


class Computer:
    def __init__(self, filename):
        self.data = open(filename).read().splitlines()
        self.running = True
        self.total = 0
        self.idx = 0
        self.CHUNK_SIZE = 50
        self.instructions = []
        self.previous = set()

    def cycle_loop(self):
        idxs = next(self.check_repeats())[0]
        idxs = [int(c) for c in idxs]
        for i in idxs:
            self.execute(self.data[i])

    def cycle(self):
        while self.running:
            print(self.total)
            self.execute(self.data[self.idx])

    def generate_instructions(self):
        for i in range(self.CHUNK_SIZE):
            self.parse(self.data[self.idx])

    def largest_substring(self):
        # codereview.stackexchange.com/questions/63329/
        string = "".join([str(i) for i in self.instructions])
        print(string)
        line = list(string)
        d = deque(string[1:])
        match = []
        longest_match = []
        while d:
            for i, item in enumerate(d):
                if line[i] == item:
                    match.append(item)
                else:
                    if len(longest_match) < len(match):
                        longest_match = match
                    match = []
            d.popleft()
        return "".join(longest_match)

    def check_repeats(self):
        # stackoverflow.com/questions/9079797
        s = "".join([str(i) for i in self.instructions])
        r = re.compile(r"(.+?)\1+")
        for match in r.finditer(s):
            yield (match.group(1), len(match.group(0)) / len(match.group(1)))

    def parse(self, ins):
        ins, val = ins.split(" ")
        op = val[0]
        num = int(val[1:])

        if ins == "nop":
            self.idx += 1
            self.instructions.append(self.idx)
            return
        elif ins == "jmp":
            if op == "+":
                self.idx = self.idx + num
                self.previous.add(self.idx)
                self.instructions.append(self.idx)
            else:
                self.idx = self.idx - num
                self.previous.add(self.idx)
                self.instructions.append(self.idx)
        elif ins == "acc":
            self.idx += 1
            self.previous.add(self.idx)
            self.instructions.append(self.idx)

    def execute(self, ins):
        print(ins)
        ins, val = ins.split(" ")
        op = val[0]
        num = int(val[1:])

        if ins == "nop":
            self.idx += 1
            self.previous.add(self.idx)
        elif ins == "jmp":
            if op == "+":
                self.previous.add(self.idx)
                self.idx = self.idx + num
            else:
                self.previous.add(self.idx)
                self.idx = self.idx - num
            if self.idx in self.previous:
                print(self.previous, self.idx)
                self.running = False
        elif ins == "acc":
            if op == "+":
                self.total += num
            else:
                self.total -= num
            self.previous.add(self.idx)
            self.idx += 1


c = Computer("input.txt")
# c.generate_instructions()
c.cycle()
print(c.total)
