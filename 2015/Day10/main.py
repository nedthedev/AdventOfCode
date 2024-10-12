#!/usr/bin/python3

DATA = """1321131112"""

def read_aloud(data):
	converted = ""
	instances = 0
	i = 0
	while(i < (len(data))):
		start = i
		while(i < len(data) - 1 and data[i] == data[i+1]):
			i+=1
		instances = i - (start - 1)
		converted += (str(instances) + str(data[start]))
		i+=1
	return converted

def part_one(data, iterations):
	answer = data
	for i in range(iterations):
		answer = read_aloud(answer)
	return answer

def part_two(data, iterations):
	return part_one(data, iterations)

if __name__ == "__main__":
	print(len(part_one(DATA, 40)))
	print(len(part_two(DATA, 50)))