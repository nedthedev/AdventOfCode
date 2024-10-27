#!/usr/bin/python3

DATA = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1""".split("\n")

TEST = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3""".split("\n")

def parse(data):
	ings = { }
	for ing in data:
		ing = ing.split(" ")
		name = ing[0][:-1]
		ings[name] = { }
		ings[name][ing[1]] = int(ing[2][:-1])
		ings[name][ing[3]] = int(ing[4][:-1])
		ings[name][ing[5]] = int(ing[6][:-1])
		ings[name][ing[7]] = int(ing[8][:-1])
		ings[name][ing[9]] = int(ing[10])
	return ings

def get_next(data, max):
	i = len(data)-1
	if(data[i] == max):
		while(i > 0 and data[i] == max):
			data = data[:i] + [1] + data[i+1:]
			i -= 1
		if(not i == 0):
			data = data[:i] + [data[i]+1] + data[i+1:]
		else:
			data = [data[0]+1] + data[i+1:]
	else:
		data = data[:len(data)-1] + [data[-1]+1]
	return data

def sum_array(arr):
	sum = 0
	for i in arr:
		sum += i
	return sum

def final_score(score, part_one):
	answer = 1
	if(not part_one and not score['calories'] == 500):
		return None 	
	for rank in score:
		if(not rank == 'calories'):
			answer *= score[rank]
	return answer

def set_zeros(data):
	for key in data:
		if(data[key] < 0):
			data[key] = 0
	return data

def get_score(ingredients, portions, part_one=False):
	score = { }
	for i, ingredient in enumerate(ingredients):
		for rank in ingredients[ingredient]:
			if(rank not in score):
				score[rank] = 0
			tmp = ingredients[ingredient][rank]
			score[rank] += (tmp * portions[i])
	return final_score(set_zeros(score), part_one)

def experiment(ingredients, portions, servings, part_one=False):
	max = servings-len(ingredients)+1
	score = tmp = 0
	optimal = []
	while(not portions[0] > max):
		portions = get_next(portions, max)
		if(sum_array(portions) == servings):
			tmp = get_score(ingredients, portions, part_one)
			if(tmp and tmp > score):
				optimal = portions
				score = tmp
	# print(optimal)
	return score

def part_one(ingredients, portions, servings):
	return experiment(ingredients, portions, servings, True)

def part_two(ingredients, portions, servings):
	return experiment(ingredients, portions, servings)

if __name__ == "__main__":
	data = parse(DATA)
	print(part_one(data, [1]*len(data), 100))
	print(part_two(data, [1]*len(data), 100))