from maze import MazeGame

def main():
    "Input maze"
    MAZE = '''
##########
#        #
#  # # # #
#B #   #E#
##########
'''
    print(MAZE.strip())
    game = MazeGame.fromString(MAZE)
    solution = game.getSolution()
    print("Length of shortest path is", solution.length(),"and steps are:")
    for step,pos in enumerate(solution):
        print("{0}. Step to {1[0]}, {1[1]}".format(step, pos))

if __name__ == '__main__':
    main()

