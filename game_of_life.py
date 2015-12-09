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
from collections import OrderedDict

class Grid(object):
	''' Base class for grid, a list of lists.

	To add:
		- A way to accept patterns
	'''

	def __init__(self, size):
		self.size = size
		self.empty_cell = "|_"
		self.grid = OrderedDict()
		for x in range(self.size):
			for y in range(self.size):
				key = str(x) + '-' + str(y)
				self.grid[key] = self.empty_cell

	def print_(self):
		''' Joins values of the grid dictionary, '''
		for i in range(self.size):
			row_idx = str(i) + '-'
			row_keys = filter(lambda key: key if key.startswith(row_idx)
								else None, self.grid.keys())
			row = [self.grid[e] for e in row_keys]
			print ''.join(row)
		return

class Universe(object):
	''' An iterator that steps through 'epochs' of the universe;
	inhabitants guided by the rules of John Conway's Game of Life.

	:max_epoch: Maximum age.
	:rate: Speed of each iteration, default is set to 0.5s.

	'''

	def __init__(self, max_epoch, rate=0.5):
		self.grid = None
		self.size = 0
		self.rate = rate
		self.cell = '|O'
		self.blank = '|_'
		self.max_epoch = max_epoch

	def construct_world(self, size):
		''' Builds the Game of Life grid as size * size board. '''

		self.size = size
		self.grid = OrderedDict()
		for x in range(size):
			for y in range(size):
				key = str(x) + '-' + str(y)
				self.grid[key] = self.blank
		return 'Board constructed.'

	def populate(self, *args, **kwargs):
		''' Populate initial state of world with cells.

		:args: - Can be unlimited positional arguments
					or list of keys format `x-y`.
		:kwargs: - Accepts keyword "pattern", which
					formats world to a preset state.
		'''
		# manual population
		if type(args[0]) is list:
			print 'this is a list'
			args = args[0]
		for arg in args:
			self.grid[arg] = self.cell
		# patterns
		for pattern in kwargs:
			if pattern == 'glider':
				pass

		return

	def __str__(self):
		return "A {s} X {s} Universe - with ".format(s=self.size) +\
				"lifespan of {a} epochs.".format(a=self.max_epoch)

	def __iter__(self):
		self.epoch = 0
		return self

	def display(self):
		''' Joins values of the grid dictionary, '''
		for i in range(self.size):
			row_idx = str(i) + '-'
			row_keys = filter(lambda key: key if key.startswith(row_idx)
								else None, self.grid.keys())
			row = [self.grid[e] for e in row_keys]
			print ''.join(row)
		return

	def next(self):
		''' Runs an update on the world. '''

		if self.epoch > self.max_epoch:
			raise StopIteration
		print "EPOCH # -- %s" % self.epoch
		sleep(self.rate)
		size = self.size
		inhabited = lambda key: True if self.grid[key] == \
								self.cell else False
		next_gen_life = []
		next_gen_death = []

		for key in self.grid.keys():

			neighbors = self.find_neighbors(key)
			if neighbors <= 1 and inhabited(key):  # underpopulation
				next_gen_death.append((key))
			elif neighbors == 3 and not inhabited(key):  # ideal for life
				next_gen_life.append((key))
			elif 2 <= neighbors <= 3:  # sustainable
				continue
			else:  # overpopulation
				next_gen_death.append((key))

		for key in next_gen_life:
			self.grid[key] = self.cell
		for key in next_gen_death:
			self.grid[key] = self.blank
		self.epoch += 1

		return self.display()

	def find_neighbors(self, key):
		''' Finds # of neighbors of cell at given address, `key`. '''

		neighbors = 0
		out_bound = lambda key_comp: True if key_comp <= 0 or\
									key_comp >= self.size else False
		key_x, key_y = key.split('-')
		key_x, key_y = int(key_x), int(key_y)

		for n_x in xrange(key_x-1, key_x+2):
			for n_y in xrange(key_y-1, key_y+2):

				if (n_x, n_y) != (key_x, key_y):
					if out_bound(n_x) or out_bound(n_y):
						continue

					key = str(n_x) + '-' + str(n_y)
					if self.grid[key] == self.cell:
						neighbors += 1
		return neighbors


game_of_life = Universe(max_epoch=10, rate=0.3)
game_of_life.construct_world(50)


game_of_life.populate(['7-6', '7-7', '8-6', '8-7', '9-7', '10-7', '11-7'])
game_of_life.populate(['7-9', '8-9', '8-10', '9-9', '7-10', '10-9', '11-9'])

print game_of_life.display()

for i in game_of_life:
	print i

