#!/usr/bin/python3

DATA = """Faerun to Tristram = 65
Faerun to Tambi = 129
Faerun to Norrath = 144
Faerun to Snowdin = 71
Faerun to Straylight = 137
Faerun to AlphaCentauri = 3
Faerun to Arbre = 149
Tristram to Tambi = 63
Tristram to Norrath = 4
Tristram to Snowdin = 105
Tristram to Straylight = 125
Tristram to AlphaCentauri = 55
Tristram to Arbre = 14
Tambi to Norrath = 68
Tambi to Snowdin = 52
Tambi to Straylight = 65
Tambi to AlphaCentauri = 22
Tambi to Arbre = 143
Norrath to Snowdin = 8
Norrath to Straylight = 23
Norrath to AlphaCentauri = 136
Norrath to Arbre = 115
Snowdin to Straylight = 101
Snowdin to AlphaCentauri = 84
Snowdin to Arbre = 96
Straylight to AlphaCentauri = 107
Straylight to Arbre = 14
AlphaCentauri to Arbre = 46""".split("\n")

TEST = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".split("\n")

class Location:
	def __init__(self, neighbors, name):
		self.neighbors = neighbors
		self.name = name
		self.reset()

	def reset(self):
		self.min_dist = 10000
		self.children = []
		self.parents = []

def parse(data):
	map = {}
	for dist in data:
		dist = dist.split(" ")
		if(dist[0] not in map):
			map[dist[0]] = Location({}, dist[0])
		if(dist[2] not in map):
			map[dist[2]] = Location({}, dist[2])
		map[dist[0]].neighbors[dist[2]] = int(dist[4])
		map[dist[2]].neighbors[dist[0]] = int(dist[4])
	return map

# def dfs(data, location, weight, path): # BORKED! (KEEPING TO DOCUMENT MY BLUNDER)
# 	if(len(path) == len(data.keys())):
# 		print(path)
# 		return (weight)
# 	else:
# 		for n in location.neighbors:
# 			# new_weight = 999
# 			# print(f"Status\nConsidering: {n}\nPath: {path}\nCurrently in: {location.name}\nDistance: {weight}\n")
# 			if(n not in path):
# 				return dfs(data, data[n], weight+location.neighbors[n], path+[n])

def dfs(data, location, distance, path, shortest, optimal):
	if(len(path) == len(data.keys())):
		if(optimal):
			if(distance < shortest):
				return distance
		else:
			if(distance > shortest):
				return distance
	for hop in location.neighbors:
		if hop not in path:
			tmp = dfs(data, data[hop], distance+location.neighbors[hop], path+[hop], shortest, optimal)
			if(optimal):
				if(tmp < shortest):
					shortest = tmp
			else:
				if(tmp > shortest):
					shortest = tmp
	return shortest

def part_one(data, fastest=True):
	if(fastest):
		shortest = 9999
	else:
		shortest = 0
	for n in data:
		dist = dfs(data, data[n], 0, [n], shortest, fastest)
		if(fastest):
			if(dist < shortest):
				shortest = dist
		else:
			if(dist > shortest):
				shortest = dist
	return shortest

def part_two(data, fastest):
	return part_one(data, fastest)

if __name__ == "__main__":
	data = parse(DATA)
	print(part_one(data))
	print(part_two(data, False))