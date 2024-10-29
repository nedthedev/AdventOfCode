#!/usr/bin/python3

DATA = """50
44
11
49
42
46
18
32
26
40
21
7
18
43
10
47
36
24
22
40""".split("\n")

TEST = """20
15
10
5
5""".split("\n")

def get_combinations(containers):
	combos = []
	bin = ''
	for i in range(1, 2**(len(containers))):
		bin = '{0:b}'.format(i)
		if(len(bin) < len(containers)+1):
			bin = ('0' * (len(containers) - len(bin))) + bin
		combos.append(bin)
	return combos

def parse(data):
	parsed = []
	for size in data:
		parsed.append(int(size))
	parsed.sort(reverse=True)
	return parsed

def part_one(data, combinations, liters):
	tmp = valid = 0
	for combination in combinations:
		tmp = 0
		for i, container in enumerate(combination):
			if(container == '1'):
				tmp += data[i]
		if(tmp == liters):
			valid += 1
	return valid

def part_two(data, combinations, liters):
	tmp = valid = containers = 0
	min = len(data)
	for combination in combinations:
		tmp = containers = 0
		for i, container in enumerate(combination):
			if(container == '1'):
				containers += 1
				tmp += data[i]
		if(tmp == liters):
			if(containers == min):
				valid += 1
			elif(containers < min):
				min = containers
				valid = 1
	return valid

if __name__ == "__main__":
	data = parse(DATA)
	combinations = get_combinations(data)
	print(part_one(data, combinations, 150))
	print(part_two(data, combinations, 150))