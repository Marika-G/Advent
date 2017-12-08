#!/usr/bin/python3

array = []
sum = 0

with open('input.txt', 'r') as input:
	i = input.read(1)
	while(i != '\n'):
		array.append(int(i))
		i = input.read(1)


j = 0
for i in range (1, len(array)):
	if(array[j] == array[i]):
		sum += array[j]
	j+=1
if(array[len(array)-1] == array[0]):
	sum += array[0]

'''
for i in array:
	print(i)
''' 
print(sum)
