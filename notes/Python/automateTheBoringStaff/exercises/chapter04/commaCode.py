#!/bin/python3

def andList(list):
	for i in range(len(list)):
		if i<len(list)-1:
			print (list[i] + ',',end='')
		else:
			print(' and ' + list[i])

spam = ['apples','bananas','tofu','cats']
andList(spam)
