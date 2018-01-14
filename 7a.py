parents = set()
enfants = set()

with open("input.txt") as progs:
    for line in progs:
        words = line.split()
        parents.add(words[0])
        if len(words) > 2:
            for i in range (3, len(words)):
                if words[i][-1] == ',':
                    words[i] = words[i][:-1]
                enfants.add(words[i])

for p in parents:
    if p not in enfants:
        print(p)
        break

