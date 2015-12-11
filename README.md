## John Conway's Game of Life

More information [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
Inspired by [Edwin Martin's](http://www.bitstorm.org/gameoflife/) implementation online.

![Imgur](http://i.imgur.com/0Haitkx.png)

This is a command-line "mini" implementation. For smaller patterns/grids (worlds),
this is ideal. Otherwise it's clunkier for things like Gosper's Glider Gun, since the
grid is printed frame-by-frame separated by a specified interval.

The idea was to contain the game grid and logic into a single Python class, an iterator, 
so that the user can "flip" through time periods of the game using a loop on an instance
of the class. 

The exposed parts of the interface include setting the max number of iterations (epochs), 
the rate at which frames are printed, and a limit on number of rows per frame 
to be printed onto the command-line.

I hope to port my implementation online as a mini-project in the future.

## How it works

Create a Universe object. The only paramater you need to set is 'max-epoch'.
``` 
game_of_life = Universe(100)
```

Construct the game grid at NxN size.
```
game_of_life.construct_world(25)
```

Populate with cells. Below are coordinates for a "glider". Coordinates are 'X-Y'.
```
game_of_life.populate(['14-13', '14-14', '14-15', '13-15', '12-14'])
```

Iterate through each frame, until the "world ends".
```
for epoch in game_of_life:
	epoch
```

_Enjoy_!
