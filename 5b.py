pas = 0

with open('input.txt', 'r') as chemin:
	instructions = [int(ligne) for ligne in chemin]

position = 0
while(True):
	try:
		offset = instructions[position]
		if(offset >= 3):
			instructions[position] -= 1
		else:
			instructions[position] += 1
		position += offset
		pas += 1

	except IndexError:
		print(pas)
		break
