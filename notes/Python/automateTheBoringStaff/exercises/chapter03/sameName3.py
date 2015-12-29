#!/bin/python3

def spam():
	global eggs
	eggs = 'spam'	#This is the global

def bacon():
	eggs = 'bacon'	#This is the local

def ham():
	print(eggs)	#This is the global

eggs = 42 #This is the global
spam()
print(eggs)
