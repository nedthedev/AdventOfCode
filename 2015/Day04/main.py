#!/usr/bin/python3

import hashlib

DATA = "iwrupvqb"

def part_one(data, zeros):
	md5 = None
	salt = 0
	while(True):
		md5 = hashlib.md5(f"{data}{salt}".encode()).hexdigest()
		if(md5[0:zeros] == ("0"*zeros)):
			return f"{data}{salt}"
		salt += 1

def part_two(data, zeros):
	return part_one(data, zeros)

if __name__ == "__main__":
	print(part_one(DATA, 5))
	print(part_two(DATA, 6))