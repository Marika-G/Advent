pas = 0

with open('input.txt', 'r') as chemin:
	instructions = [int(ligne) for ligne in chemin]

position = 0
while(True):
	try:
		instructions[position] += 1
		position += instructions[position] - 1
		pas += 1

	except IndexError:
		print(pas)
		break
