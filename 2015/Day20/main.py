#!/usr/bin/python3

import time
import math

DATA = """36000000"""

TEST = """360"""

def part_one(data, pkg_per):
	delivered = pkg_per
	house = 0
	while(delivered < int(data)):
		house += 1
		delivered = house * pkg_per
		for i in range(1, house):
			if(house % i == 0):
				delivered += (i * pkg_per)
	return house

def part_two(data, pkg_per):
	delivered = pkg_per
	house = 0
	while(delivered < int(data)):
		house += 1
		delivered = house * pkg_per
		for i in range(math.ceil(house/50), house):
			if(house % i == 0):
				delivered += (i * pkg_per)
	return house

if __name__ == "__main__":
	print(part_one(DATA, 10))
	print(part_two(DATA, 11))
