# Maze

This module solves shortest path finding in maze.

Maze is final 2D matrix and there is either path or wall in every cell. We may go through neighbour cells but not through walls of course. Neighbour cells are such cells which meet the condition:

	abs(x1-x2) + abs(y1-y2) == 1

Maze has exactly one start and exaclty one end. These cells have to be on path.

This module implements:

- `MazeGame` class 
   - `MazeGame` contains static `fromString` method which can initialize myself from string
   - `MazeGame` contains `getSize` method which returns size of maze
   - `MazeGame` contains `isFree` method which indicates possibility to enter on cell
   - `MazeGame` contains `getStart` and `getEnd` methods which return start and end position
   - `MazeGame` contains `getSolution` method which returns shortest path from start to end as instance of `MazePath` class

- `MazePath` class represents solution of maze
   - `MazePath` contains `length` method which returns length of solution
   - `MazePath` provides an iterator which returns cells of solution

- `MazeError` exception which is thrown when unexpected situation occurred, e.g.:
   - try create maze without start or start is outside of maze
   - try create maze with two ends
   - there is no path from start to end


## Use case:
    from maze import MazeGame

    def main():
        game = MazeGame.fromString("B  \n# E")
        solution = game.getSolution()
        print("Size of maze is {0}".format(game.getSize()))
        print("Length of shortest path is {0} and steps are:".format(solution.length()))
        for step,pos in enumerate(solution):
            print("{0}. Step to {1[0]}, {1[1]}".format(step, pos))
    if __name__ == '__main__':
        main()

You may use `python maze_demo.py` or `python3 maze_demo.py` in main folder to run another example.
