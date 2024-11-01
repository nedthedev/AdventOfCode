#!/usr/bin/python3

import re
import time

DATA = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg

CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF""".split("\n")

TEST = """e => H
e => O
H => HO
H => OH
O => HH

HOH""".split("\n")

def parse(data):
	replacements = {}
	code = ""
	for line in data:
		line = line.split(" => ")
		if(len(line) > 1):
			if(line[0] not in replacements):
				replacements[line[0]] = []
			replacements[line[0]].append(line[1])
		else:
			if(not line == ""):
				code = line[0]
	return {'replacements': replacements, 'code': code}

def get_instances(code, subcode):
	return len(re.findall(subcode, code))

def replace_nth_occurence(find, replace, string, n, match_case=True):
	i = 0
	found = 0
	discovered = False
	while(i < len(string)-len(find)+1):
		discovered = False
		if(match_case):
			if(string[i:i+len(find)] == find):
				discovered = True
		else:
			if(string[i:i+len(find)].lower() == find.lower()):
				discovered = True
		if(discovered):
			found += 1
			if(found == n):
				return (string[:i] + replace + string[i+len(find):])
			i += len(find)
		else:
			i+=1
	return None

def print_tree(tree):
	print("\n")
	for row in tree:
		print(row)

# generate a search tree that will generate all the possible combinations
# then search for the molecule in the tree and we'll know the depth of that
# node is the number of replacments we needed to make
def bfs(replacements, tree, target):
	new_leaf = None
	to_append = []
	depth = 0
	while(target not in tree[-1]):
		to_append = []
		for leaf in tree[-1]:
			new_leaf = find_and_replace(replacements, leaf)
			for nl in new_leaf:
				if(nl not in to_append):
					to_append.append(nl)
		depth += 1
		tree[0] = to_append
		# print(tree[-1])
		# time.sleep(.5)
	return depth

def find_and_replace(replacements, code):
	molecules = []
	tmp = ''
	for subcode in replacements:
		for replacement in replacements[subcode]:
			for i in range(get_instances(code, subcode)):
				tmp = replace_nth_occurence(subcode, replacement, code, i+1)
				if(tmp not in molecules):
					molecules.append(tmp)
	return molecules

def part_one(replacements, code):
	return find_and_replace(replacements, code)

def part_two(replacements, tree, target):
	tree = bfs(replacements, tree, target)
	return tree

if __name__ == "__main__":
	data = parse(DATA)
	# print(len(part_one(data['replacements'], data['code'])))
	print(part_two(data['replacements'], [['e']], data['code']))