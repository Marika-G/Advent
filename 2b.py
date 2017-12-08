
array = [[]]
sum = []

with open('input2a.csv', 'r') as input:
	cap = [[int(x) for x in line.split()] for line in input]



for i in range(len(cap)):
	trouve = False
	for j in range(len(cap[i])-1):
		for k in range(j+1, len(cap[i])):
			if(cap[i][j]/cap[i][k] == cap[i][j]//cap[i][k]):
				sum.append(cap[i][j]//cap[i][k])
				trouve = True
				break
			elif(cap[i][k]/cap[i][j] == cap[i][k]//cap[i][j]):
				sum.append(cap[i][k]//cap[i][j])
				trouve = True
				break
		if(trouve): break		

totSum = 0
for k in sum:
	totSum += k
print(totSum)
