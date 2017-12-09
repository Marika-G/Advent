
tot = 0

with open('input.txt', 'r') as input:
	for line in input:
		tot += 1
		mySet = set()
		for x in line.split():
			x = ''.join(sorted(x))
			if (x not in mySet):
				mySet.add(x)
			else:
				tot -= 1
				break
print(tot)
