from maze import MazeGame

def main():
    "Input maze"
    MAZE = '''
#################
#              E#
### #############
###           ###
####### #########
#B              #
#################
'''

    print(MAZE)
    game = MazeGame.fromString(MAZE)
    solution = game.getSolution()
    print("Size of maze is {0}".format(game.getSize()))
    print("Length of shortest path is {0} and steps are:".format(solution.length()))
    for step,pos in enumerate(solution):
        print("{0}. Step to {1[0]}, {1[1]}".format(step, pos))

if __name__ == '__main__':
    main()

