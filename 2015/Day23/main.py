#!/usr/bin/python3

import time

DATA = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7""".split("\n")

TEST = """inc a
jio a, +1
tpl a
inc a""".split("\n")

def run_instruction(instruction, state):
	instruction = instruction.replace(",", "")
	instruction = instruction.split(" ")
	line_was = state['line']
	match instruction[0]:
		case 'hlf':
			state[instruction[1]] = state['a']//2
		case 'tpl':
			state[instruction[1]] *= 3
		case 'inc':
			state[instruction[1]] += 1
		case 'jmp':
			state['line'] += int(instruction[1])
		case 'jie':
			if(state[instruction[1]] % 2 == 0): 
				if(instruction[2][0] == "+"):
					state['line'] += int(instruction[2])
				else:
					state['line'] -= int(instruction[2])
		case 'jio':
			if(state[instruction[1]] == 1): 
				if(instruction[2][0] == "+"):
					state['line'] += int(instruction[2])
				else:
					state['line'] -= int(instruction[2])
	if(state['line'] == line_was): state['line'] += 1
	return state

def run(program, state):
	while(state['line'] < len(program)):
		state = run_instruction(program[state['line']], state)
	return state

def part_one(data):
	return run(data, {'a': 0, 'b': 0, 'line': 0})['b']

def part_two(data):
	return run(data, {'a': 1, 'b': 0, 'line': 0})['b']

if __name__ == "__main__":
	print(part_one(DATA))
	print(part_two(DATA))