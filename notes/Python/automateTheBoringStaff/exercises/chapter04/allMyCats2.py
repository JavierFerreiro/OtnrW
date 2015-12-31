#!/bin/python3

catNames = []
while True:
	print('Introduce the name of the cat: ',end='')
	name = input()
	if name == '':
		break
	catNames.append(name)

print('The name of the cats are:')
for name in catNames:
	print(name)
	
