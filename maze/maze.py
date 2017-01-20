# coding: utf-8 
from .exceptions import MazeError
from collections import deque
import numpy

class MazeGame(object):

    def __init__(self, data, start, end):
        """Init maze
        data is 2D matrix , 
        start is position of begining , e.g. [1,1]
        end is position of goal, e.g. [10,10].

        Pokud start nebo stop je mimo bludiste, vyvola vyjimku
        When start or end is outside of maze, exception occur
        """
        assert data.dtype == bool
        
        self.data = data
        
        if (start[0]<0) or (start[0]>=self.getSize()[0]) or (start[1]<0) or (start[1]>=self.getSize()[1]):
            raise MazeError("Start position is out of maze")
        if (end[0]<0) or (end[0]>=self.getSize()[0]) or (end[1]<0) or (end[1]>=self.getSize()[1]):
            raise MazeError("End position is out of maze")
        
        self.start = start
        self.end = end
        

    def getSize(self):
        "Return maze size"
        return self.data.shape

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end

    def isFree(self, x, y):
        "Return False when there is a wall on position x,y. Else return True"
        if (x<0) or (x>=self.getSize()[0]) or (y<0) or (y>=self.getSize()[1]):
            return False
        return self.data[x,y]                    

    def getSolution(self):
        "Return some shortest maze solution or an exception occure"
        
        queue = deque([("b", self.start)])
        visited = set()
        while queue:
            path, current = queue.popleft()
            if current == self.end:
                """We found the end!
                   In variable path is string of directions how to get from start to end.
                   d = down, u = up, r = right, l = left"""
                print(path)
                break
            if current in visited:
                continue
            visited.add(current)
            if (self.isFree(current[0]+1,current[1])):
                queue.append((path+"d", (current[0]+1,current[1])))
            if (self.isFree(current[0]-1,current[1])):
                queue.append((path+"u", (current[0]-1,current[1])))
            if (self.isFree(current[0],current[1]+1)):
                queue.append((path+"r", (current[0],current[1]+1)))
            if (self.isFree(current[0],current[1]-1)):
                queue.append((path+"l", (current[0],current[1]-1)))
        
        
        
        
        
        return MazePath(steps=[])

    @staticmethod 
    def fromString(maze):
        """
        Build maze from string.
        Empty lines are ignored, 
        X or # is wall,  B represents start and E represents goal of maze.
        """
        
        lines = maze.splitlines()
        
        # ... if line remove empty line
        input_data = [list(line) for line in lines if line]
        input_data = numpy.asarray(input_data)
        
        if (len(input_data.shape)<2):
            raise MazeError("Maze is not regular! Some row(s) has different length than others.")
        
        HEIGHT = input_data.shape[0]
        WIDTH = input_data.shape[1]

        data = numpy.empty((HEIGHT,WIDTH),dtype=bool)

        start_count, end_count = 0, 0

        for i in range(HEIGHT):
            for j in range(WIDTH):
                if (input_data[i,j] == 'X') or (input_data[i,j] == '#'):
                    data[i,j] = False
                elif input_data[i,j] == 'B':
                    if start_count>0:
                        raise MazeError("Too many begins!")
                    start_count += 1
                    start = (i,j)
                    data[i,j] = True
                elif input_data[i,j] == 'E':
                    if end_count > 0:
                        raise MazeError("Too many ends!")
                    end_count += 1
                    end = (i,j)
                    data[i,j] = True
                else:
                    data[i,j] = True
                
            
        if start_count == 0:
            raise MazeError("There is no begin!")
        if end_count == 0:
            raise MazeError("There is no end!")
        
        return MazeGame(data, start, end)

class MazePath(object):
    "Objekt obsahujici cestu v bludisti"

    def __init__(self, steps):
        "Inicializuje objekt MazePath"
        pass

    def length(self):
        "Vraci delku cesty v bludisti"
        return 0

    def __iter__(self):
        "Iterator vracejici jednotlive body cesty"
        yield (0,0)
        yield (0,1)
        yield (1,1)
