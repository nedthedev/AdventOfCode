#!/usr/bin/python3

import time

DATA = """hepxcrrq"""

def has_three_consec(data):
	is_good = False
	for i in range(0, len(data)-2):
		value = ord(data[i])
		for j in range(i+1, i+3):
			if(not(ord(data[j]) == value+1)):
				is_good = False
				break
			else:
				value += 1
				is_good = True
		if(is_good):
			return True
	return False

def has_two_doubles(data):
	pairs = 0
	i = 0
	while(i < len(data)-1):
		if(data[i+1] == data[i]):
			i += 1
			pairs += 1
		i += 1
	return pairs >= 2

def has_no_invalids(data, invalids='iol'):
	for char in invalids:
		if(char in data):
			return False
	return True

def has_good_length(data, requirement=8):
	return len(data) >= requirement

def is_good(password):
	return (
		has_three_consec(password) and 
		has_two_doubles(password) and 
		has_no_invalids(password) and 
		has_good_length(password)
	)

def get_next(data):
	i = len(data)-1
	if(data[i] == 'z'):
		while(i > 0 and data[i] == 'z'):
			data = data[:i] + 'a' + data[i+1:]
			i -= 1
		if(not i == 0):
			data = data[:i] + chr(ord(data[i])+1) + data[i+1:]
	else:
		data = data[:len(data)-1] + chr(ord(data[-1])+1)
	return data

def cycle(data):
	password = data
	while(not is_good(password)):
		password = get_next(password)
	return password

def part_one(data):
	return cycle(data)

def part_two(data):
	return part_one(data)

if __name__ == "__main__":
	print(part_one(DATA))
	print(part_two(get_next(part_one(DATA))))