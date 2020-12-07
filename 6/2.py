with open('input.txt') as f:
    data = f.read().split('\n\n')

c = 0
for g in data:
    s = list(g.split('\n'))
    if len(s) == 1:
        c += len(s[0])

    else:
        sect = set(s[0]).intersection(*s)
        c += len(sect)

print(c)
