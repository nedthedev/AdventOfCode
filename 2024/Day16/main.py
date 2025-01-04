#!/usr/bin/python3

DATA = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".split("\n")

class Cell:
	def __init__(self, type, r, c):
		self.char = type
		self.valid = True
		self.cost = 1
		self.neighbors = []
		self.row, self.col = r, c
		match self.char:
			case '#':
				self.valid = False
			case '.':
				pass
			case 'S':
				self.cost = 0
			case 'E':
				pass
	
	def filter_neighbors(self):
		for index, n in enumerate(self.neighbors):
			if(n.char == '#'):
				del self.neighbors[index]

	def print(self):
		s = ''
		for n in self.neighbors:
			s += n.char
		print(s)

class Grid:
	def __init__(self, data):
		self.grid = []
		self.start = None
		self.end = None
		# gen cells
		for r, row in enumerate(data):
			self.grid.append([])
			for c, col in enumerate(row):
				self.grid[len(self.grid)-1].append(Cell(col, r, c))
				if(self.grid[r][c].char == 'S'):
					self.start = self.grid[r][c]
				elif(self.grid[r][c].char == 'E'):
					self.end = self.grid[r][c]
		# gen cell neighbors
		for r, row in enumerate(self.grid):
			for c, col in enumerate(row):
				if(r > 1):
					self.grid[r][c].neighbors.append(self.grid[r-1][c])
				if(r < len(self.grid)-1):
					self.grid[r][c].neighbors.append(self.grid[r+1][c])
				if(c > 1):
					self.grid[r][c].neighbors.append(self.grid[r][c-1])
				if(c < len(self.grid[0])-1):
					self.grid[r][c].neighbors.append(self.grid[r][c+1])
				self.grid[r][c].filter_neighbors()

	def navigate(self, start, end):
		current = start
		queue = start.neighbors
		while(len(queue) > 0):
			cell = queue.pop()
			if(current.weight + cell.cost < cell.weight):
				cell.weight = current.weight + cell.cost
				cell.parent = current
				queue.append(cell)

	def print(self):
		for row in self.grid:
			s = ''
			for c in row:
				s += c.char
			print(s)

def part_one(data):
	grid = Grid(data)
	grid.grid[len(grid.grid)-2][len(grid.grid)-2].print()
	grid.print()

def part_two(data):
	pass

if __name__ == "__main__":
	part_one(DATA)