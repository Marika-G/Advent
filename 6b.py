config = [5,1,10,0,1,7,13,14,3,12,8,10,7,12,0,6]
pastConfig = dict()
nbTours = 0

while(tuple(config) not in pastConfig):
	pastConfig[tuple(config)] = nbTours
	i = config.index(max(config))
	toDist = config[i]
	config[i] = 0
	while(toDist > 0):
		i = (i+1)%len(config)
		config[i] += 1
		toDist -= 1
	nbTours += 1

print(nbTours - pastConfig[tuple(config)])