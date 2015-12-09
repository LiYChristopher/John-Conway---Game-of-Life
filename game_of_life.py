''' John Conway's Game of Life 

Rules taken from http://www.bitstorm.org/gameoflife/.

For a space that is 'populated':
	Each cell with one or no neighbors dies, as if by solitude.
	Each cell with four or more neighbors dies, as if by overpopulation.
	Each cell with two or three neighbors survives.
For a space that is 'empty' or 'unpopulated'
	Each cell with three neighbors becomes populated.

'''
from time import sleep

class Grid(object):
	''' Base class for grid, a list of lists.

	To add:
		- A way to accept patterns
	'''

	def __init__(self, size):
		self.size = size
		self.empty_cell = "|_"
		self.grid = [[self.empty_cell for _ in range(self.size)]
							for _ in range(self.size)]

	def print_(self):
		for i in self.grid:
			print ''.join(i) + '|'
		return

class Universe(object):
	''' An iterator that steps through 'epochs' of the universe;
	inhabitants guided by the rules of John Conway's Game of Life.

	To add:
		- Reimplement with dictionary - faster lookup and cleaner code.

	'''

	def __init__(self, grid, max_epoch):
		self.grid = grid
		self.cell = '|O'
		self.blank = '|_'
		self.max_epoch = max_epoch

	def __iter__(self):
		self.epoch = 0
		self.world = grid.grid
		return self

	def next(self):
		if self.epoch > self.max_epoch:
			raise StopIteration
		print "EPOCH # -- %s" % self.epoch
		sleep(1)
		size = self.grid.size
		inhabited = lambda x, y: True if self.grid.grid[x][y] == \
								self.cell else False
		next_gen_life = []
		next_gen_death = []

		for x in xrange(size):
			for y in xrange(size):
				neighbors = self.find_neighbors(x, y)
				# unfavorable condition of underpopulation
				if neighbors <= 1 and inhabited(x, y):
					next_gen_death.append((x, y))
				# favorable condition for life
				elif neighbors == 3 and not inhabited(x, y):
					next_gen_life.append((x, y))
				# favorable condition for sustainability
				elif 2 <= neighbors <= 3:
					continue
				# unfavorable condition of overpopulation
				elif neighbors >= 4:
					next_gen_death.append((x, y))

		for coords in next_gen_life:
			x, y = coords
			self.grid.grid[x][y] = self.cell
		for coords in next_gen_death:
			x, y = coords
			self.grid.grid[x][y] = self.blank
		self.epoch += 1

		return self.grid.print_()

	def find_neighbors(self, x, y):
		neighbors = 0
		out_bound = lambda ny : True if ny <= 0 or ny >= 25 else False
		for nx in xrange(x-1, x+2):
			for ny in xrange(y-1, y+2):
				if (x, y) != (nx, ny):
					if out_bound(nx) or out_bound(ny):
						continue
					if self.grid.grid[nx][ny] == self.cell:
						neighbors +=1
		return neighbors


game_of_life = Universe(Grid(25), 10)

game_of_life.grid.grid[7][6] = game_of_life.cell
game_of_life.grid.grid[7][7] = game_of_life.cell
game_of_life.grid.grid[7][8] = game_of_life.cell
game_of_life.grid.grid[6][8] = game_of_life.cell
game_of_life.grid.grid[5][7] = game_of_life.cell
#game_of_life.grid.grid[6][21] = game_of_life.cell
#game_of_life.grid.grid[9][21] = game_of_life.cell
#print game_of_life.find_neighbors(4, 3)
#print game_of_life.find_neighbors(4, 5)
#print game_of_life.find_neighbors(3, 3)
for i in game_of_life:
	i

