
array = [[]]
sum = []
i = 0

with open('input2a.csv', 'r') as input:
	cap = [[int(x) for x in line.split()] for line in input]

for i in range(len(cap)):
	min = max = cap[i][0]
	for j in cap[i]:
		if(j < min):
			min = j
		if(j > max):
			max = j
	sum.append(max-min)

totSum = 0
for k in sum:
	totSum += k
print(totSum)