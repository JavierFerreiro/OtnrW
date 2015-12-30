#!/bin/python3

def collatz(number):
	if number%2 == 0:
		resul = number//2
		print(resul)
		return resul 
	else:
		resul = 3 * number + 1
		print(resul)
		return resul	

noInteger = True
while noInteger:
	try:
		print('Write a number: ')
		number = int(input())
		noInteger = False
	except ValueError:
		print('Your input is not a integer. retry please')	

while number!=1:
	number = collatz(number)

	
