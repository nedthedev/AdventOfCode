#!/usr/bin/python3

import re

BOSS = """Hit Points: 109
Damage: 8
Armor: 2""".split("\n")

SHOP = """Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Naked		  0		0		0
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3""".split("\n")

class Character:
	def __init__(self, name, hp, damage=0, armor=0):
		self.name = name
		self.max_hp = hp
		self.damage = damage
		self.armor = armor
		self.weapon = None
		self.armor_equipped = None
		self.rings = []
		self.is_victor = None
		self.reset()

	def get_damage(self):
		if(self.damage + self.damage_buff == 0):
			return 1
		return self.damage + self.damage_buff

	def get_armor(self):
		return self.armor + self.armor_buff

	def attack(self, enemy):
		enemy.defend(self.get_damage())

	def defend(self, damage):
		if(damage > self.get_armor()):
			self.hp -= (damage - self.get_armor())
		else:
			self.hp -= 1

	def finalize(self):
		self.spent = self.weapon['C']
		self.spent += self.armor_equipped['C']
		self.damage_buff = self.weapon['D']
		self.armor_buff = self.armor_equipped['A']
		for ring in self.rings:
			self.spent += ring['C']
			if(ring['A']):
				self.armor_buff += ring['A']
			else:
				self.damage_buff += ring['D']

	def battle(self, enemy):
		self.finalize()
		count = 0
		while(enemy.hp > 0 and self.hp > 0):
			if(count % 2 == 0):
				self.attack(enemy)
			else:
				enemy.attack(self)
			count += 1
		self.is_victor = self.hp > 0
		return self.is_victor
	
	def reset(self):
		self.hp = self.max_hp
		self.damage_buff = 0
		self.armor_buff = 0
		self.spent = 0
		self.is_victor = None

	def get_equipment(self):
		return f"{self.weapon}, {self.armor_equipped}, {self.rings}"

	def print(self):
		print(f"{self.name}:\n\tSpent: {self.spent}\n\tHP: {self.hp}\n\tDamage: {self.get_damage()}\n\tArmor: {self.get_armor()}\n\tEquipment: {self.get_equipment()}")

def get_combinations(items):
	combos = []
	bin = ''
	for i in range(0, 2**(len(items))):
		bin = '{0:b}'.format(i)
		if(len(bin) < len(items)+1):
			bin = ('0' * (len(items) - len(bin))) + bin
		if(len(re.findall('1', bin)) <= 2):
			combos.append(bin)
	return combos

def parse_boss(data):
	stat = ''
	character = {}
	for line in data:
		line = line.split(": ")
		stat = re.findall("['A-Z']", line[0])
		character[''.join(stat)] = int(line[1])
	return Character('Boss', character['HP'], character['D'], character['A'])

def parse_shop(data):
	items = {}
	category = None
	item = None
	offset = 0
	for line in data:
		offset = 0
		if(re.search("\\D+[:]", line)):
			category = line.split(": ")[0]
			items[category] = {}
		elif(re.search("\\d+", line)):
			item = re.findall("^[a-zA-Z]+", line)[0]
			line = re.findall("\\d+", line)
			if(category == "Rings"):
				item = f'Ring{len(items[category])}'
				items[category][item] = {}
				items[category][item]['P'] = int(line[offset])
				offset += 1
			else:
				items[category][item] = {}
			items[category][item]['C'] = int(line[offset])
			items[category][item]['D'] = int(line[offset+1])
			items[category][item]['A'] = int(line[offset+2])
	return items

def run_simulations(player, boss, shop):
	results = []
	combos = get_combinations(shop['Rings'])
	for weapon in shop['Weapons']:
		player.weapon = shop['Weapons'][weapon]
		for armor in shop['Armor']:
			player.armor_equipped = shop['Armor'][armor]
			for combo in combos:
				for i, buy in enumerate(combo):
					if(buy == '1'):
						player.rings.append(shop['Rings'][f'Ring{i}'])
				player.battle(boss)
				results.append({'spent': player.spent, 'victory': player.is_victor})
				player.rings = []
				player.reset()
				boss.reset()
			player.armor_equipped = None
		player.weapon = None
	return results

def part_one(player, boss, shop):
	results = run_simulations(player, boss, shop)
	min_spent = 10000
	for result in results:
		if(result['victory'] and result['spent'] < min_spent):
			min_spent = result['spent']
	return min_spent

def part_two(player, boss, shop):
	results = run_simulations(player, boss, shop)
	max_spent = 0
	for result in results:
		if(not result['victory'] and result['spent'] > max_spent):
			max_spent = result['spent']
	return max_spent

if __name__ == "__main__":
	player = Character('You', 100, 0, 0)
	boss = parse_boss(BOSS)
	shop = parse_shop(SHOP)
	print(part_one(player, boss, shop))
	print(part_two(player, boss, shop))
	