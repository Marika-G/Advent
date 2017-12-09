#jour3b


'''
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806  854  905
'''
ref = 854
grid = [[0]*99]*99
grid[49][49] = 1
pos_x = 50
pos_y = 49
grid[pos_x][pos_y] = 1
value = 0


while(grid[pos_x-1][pos_y] != 0):
	pos_y -=1
	value = grid[pos_x+1][pos_y] + grid[pos_x+1][pos_y+1] + grid[pos_x][pos_y+1] + grid[pos_x-1][pos_y+1] +  grid[pos_x-1][pos_y] + grid[pos_x-1][pos_y-1] + grid[pos_x][pos_y-1] + grid[pos_x+1][pos_y-1]
	grid[pos_x][pos_y] = value
	print(value)
	print("\n")

while(grid[pos_x][pos_y+1] != 0):
	pos_x -= 1
	value = grid[pos_x+1][pos_y] + grid[pos_x+1][pos_y+1] + grid[pos_x][pos_y+1] + grid[pos_x-1][pos_y+1] +  grid[pos_x-1][pos_y] + grid[pos_x-1][pos_y-1] + grid[pos_x][pos_y-1] + grid[pos_x+1][pos_y-1]
	grid[pos_x][pos_y] = value
	print(value)
	print("\n")

while(grid[pos_x+1][pos_y] != 0):
	pos_y += 1
	value = grid[pos_x+1][pos_y] + grid[pos_x+1][pos_y+1] + grid[pos_x][pos_y+1] + grid[pos_x-1][pos_y+1] +  grid[pos_x-1][pos_y] + grid[pos_x-1][pos_y-1] + grid[pos_x][pos_y-1] + grid[pos_x+1][pos_y-1]
	grid[pos_x][pos_y] = value
	print(value)
	print("\n")

while(grid[pos_x][pos_y-1] != 0):
	pos_x += 1
	value = grid[pos_x+1][pos_y] + grid[pos_x+1][pos_y+1] + grid[pos_x][pos_y+1] + grid[pos_x-1][pos_y+1] +  grid[pos_x-1][pos_y] + grid[pos_x-1][pos_y-1] + grid[pos_x][pos_y-1] + grid[pos_x+1][pos_y-1]
	grid[pos_x][pos_y] = value
	print(value)
	print("\n")

	


