''' John Conway's Game of Life

Rules taken from http://www.bitstorm.org/gameoflife/.

For a space that is 'populated':
	1) Each cell with one or no neighbors dies, as if by solitude.
	2) Each cell with four or more neighbors dies, as if by overpopulation.
	3) Each cell with two or three neighbors survives.
For a space that is 'empty' or 'unpopulated'
	Each cell with three neighbors becomes populated.
'''

from time import sleep
from collections import OrderedDict
from colorama import Fore, Style, init


class Universe(object):
	''' An iterator that steps through 'epochs' of the universe;
	inhabitants guided by the rules of John Conway's Game of Life.

	:max_epoch: Maximum age.
	:rate: Speed of each iteration, default is set to 0.5s.
	:disp_limit: Sets limit for rows displayed in each frame, so the
	world is a little more viewable when it's larger than ~30-40 rows.

	'''

	def __init__(self, max_epoch, rate=0.5, disp_limit=50):
		self.grid = None
		self.size = 0
		self.rate = rate
		self.cell = Fore.GREEN + Style.BRIGHT + '|O'
		self.blank = Fore.BLACK + Style.BRIGHT + '|_'
		self.max_epoch = max_epoch
		self.display_limit = self.size or disp_limit

	def construct_world(self, size):
		''' Builds the Game of Life grid as size * size board. '''

		self.size = size
		self.grid = OrderedDict()
		for x in range(size):
			for y in range(size):
				key = str(x) + '-' + str(y)
				self.grid[key] = self.blank
		return 'Board constructed.'

	def populate(self, *args):
		''' Populate initial state of world with cells.

		:args: - Can be unlimited positional arguments
					or list of keys format `x-y`.
		'''
		# manual population
		if type(args[0]) is list:
			args = args[0]
		for arg in args:
			self.grid[arg] = self.cell
		return

	def __str__(self):
		return "A {s} X {s} Universe - with ".format(s=self.size) +\
				"lifespan of {a} epochs.".format(a=self.max_epoch)

	def __iter__(self):
		self.epoch = 0
		init(autoreset=True)
		return self

	def display(self):
		''' Joins values of the grid dictionary, '''
		for i in range(self.display_limit):
			row_idx = str(i) + '-'
			row_keys = filter(lambda key: key if key.startswith(row_idx)
								else None, self.grid.keys())
			row = [self.grid[e] for e in row_keys]
			print ''.join(row)
		return

	def next(self):
		''' Runs activities of one epoch in simulation. '''
		if self.epoch > self.max_epoch:
			raise StopIteration

		sleep(self.rate)
		size = self.size
		inhabited = lambda key: True if self.grid[key] == \
								self.cell else False

		next_gen_life, next_gen_death = [[], []]

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
		print Fore.WHITE + Style.BRIGHT + "EPOCH # -- %s" % self.epoch
		self.display()
		return

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

if __name__ == '__main__':

	# examples below, just uncomment. 
	game_of_life = Universe(max_epoch=500, rate=0.075, disp_limit=37)
	game_of_life.construct_world(60)

	# Glider
	#game_of_life.populate(['14-13', '14-14', '14-15', '13-15', '12-14'])

	# Tumbler
	game_of_life.populate(['7-6', '7-7', '8-6', '8-7', '9-7', '10-7', '11-7'])
	game_of_life.populate(['7-9', '8-9', '8-10', '9-9', '7-10', '10-9', '11-9'])
	game_of_life.populate(['10-5', '11-5', '12-5', '12-6'])
	game_of_life.populate(['10-11', '11-11', '12-11', '12-10'])

	# Mini Exploder
	#game_of_life.populate(['9-10', '9-11', '9-12', '10-10', '10-12', '8-11', '11-11'])

	# Gosper's Glider Gun
	#game_of_life.populate(['15-10', '15-11', '16-10', '16-11'])
	#game_of_life.populate(['15-19', '15-20', '16-18', '16-20', '17-18', '17-19'])
	#game_of_life.populate(['17-26', '17-27', '18-26', '18-28', '19-26'])
	#game_of_life.populate(['13-33', '13-34', '14-32', '14-34', '15-32', '15-33'])
	#game_of_life.populate(['13-44', '13-45', '14-44', '14-45'])
	#game_of_life.populate(['13-44', '13-45', '14-44', '14-45'])
	#game_of_life.populate(['20-45', '20-46', '21-45', '21-47', '22-45'])
	#game_of_life.populate(['25-34', '25-35', '25-36', '26-34', '27-35'])

	game_of_life.display()
for epoch in game_of_life:
	epoch
