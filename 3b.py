#jour3b


'''
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806  854  905 
'''
def imprime(table):
	for i in table:
		for el in i:
			print(el, end='\t')
		print("")
	print("")

def findNext(ref):
	grid = [[0]*25 for i in range(26)]
	imprime(grid)
	grid[12][12] = 1
	ligne = 12
	colonne = 13
	grid[ligne][colonne] = 1
	imprime(grid)
	value = 0

	while(True):
		while(grid[ligne][colonne-1] != 0):
			ligne -=1
			value = grid[ligne+1][colonne] + grid[ligne+1][colonne+1] + grid[ligne][colonne+1] + grid[ligne-1][colonne+1] +  grid[ligne-1][colonne] + grid[ligne-1][colonne-1] + grid[ligne][colonne-1] + grid[ligne+1][colonne-1]
			grid[ligne][colonne] = value
			if(value > ref):
				print(value)
				imprime(grid)
				return

		while(grid[ligne+1][colonne] != 0):
			colonne -= 1
			value = grid[ligne+1][colonne] + grid[ligne+1][colonne+1] + grid[ligne][colonne+1] + grid[ligne-1][colonne+1] +  grid[ligne-1][colonne] + grid[ligne-1][colonne-1] + grid[ligne][colonne-1] + grid[ligne+1][colonne-1]
			grid[ligne][colonne] = value
			if(value > ref):
				print(value)
				imprime(grid)
				return

		while(grid[ligne][colonne+1] != 0):
			ligne += 1
			value = grid[ligne+1][colonne] + grid[ligne+1][colonne+1] + grid[ligne][colonne+1] + grid[ligne-1][colonne+1] +  grid[ligne-1][colonne] + grid[ligne-1][colonne-1] + grid[ligne][colonne-1] + grid[ligne+1][colonne-1]
			grid[ligne][colonne] = value
			if(value > ref):
				print(value)
				imprime(grid)
				return

		while(grid[ligne-1][colonne] != 0):
			colonne += 1
			value = grid[ligne+1][colonne] + grid[ligne+1][colonne+1] + grid[ligne][colonne+1] + grid[ligne-1][colonne+1] +  grid[ligne-1][colonne] + grid[ligne-1][colonne-1] + grid[ligne][colonne-1] + grid[ligne+1][colonne-1]
			grid[ligne][colonne] = value
			if(value > ref):
				print(value)
				imprime(grid)
				return

	
findNext(368078)

