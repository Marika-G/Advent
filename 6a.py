config = [5,1,10,0,1,7,13,14,3,12,8,10,7,12,0,6]
pastConfig = set()

while(tuple(config) not in pastConfig):
	pastConfig.add(tuple(config))
	i = config.index(max(config))
	toDist = config[i]
	config[i] = 0
	while(toDist > 0):
		i = (i+1)%len(config)
		config[i] += 1
		toDist -= 1

print(len(pastConfig))