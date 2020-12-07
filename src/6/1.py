with open('input.txt') as f:
    data = f.read().split('\n\n')

c = 0
for g in data:
    s = set()
    for i in g:
        if i != '\n':
            s.add(i.strip())
    c += len(s)
print(c)
