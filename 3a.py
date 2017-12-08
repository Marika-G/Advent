#jour3

input = 368078
i = 1
p = 1
while(p < input):
	i = i+2
	p = i*i

pas = p - input
pas = abs((i-1)/2 - pas%(i-1))
distance = (i-1)/2 + pas

print(distance)