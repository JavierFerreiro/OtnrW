#!/bin/python3

myPets=['Jander','Clander','Mene','Moguer']

print('Enter a pet name:',end='')
petName = input()

if petName in myPets:
	print(petName + ' is my pet')
else:
	print('I do not have a pet named' + petName)

