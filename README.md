## John Conway's Game of Life

More information here:

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

![alt tag]img/GOL img.tiff

This is a command-line "mini" implementation. For smaller patterns/grids (worlds),
this is ideal. Otherwise it's clunkier for things like Gosper's Glider Gun, since the
grid is printed frame-by-frame separated by a specified interval.

The idea was to contain the game grid and logic into a single Python class, an iterator, 
so that the user can "flip" through time periods of the game using a loop on an instance
of the class. 

The exposed parts of the interface include setting the max number of iterations (epochs), 
the rate at which frames are printed, and a limit on number of rows per frame 
to be printed onto the command-line.

Enjoy!