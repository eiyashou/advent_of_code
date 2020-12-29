from dataclasses import dataclass, field
from operator import itemgetter
from collections import deque


class Pos:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __add__(self, o):
        return Pos(self.x+o.x, self.y+o.y)
    
    def __hash__(self):
        return hash((self.x,self.y))
    
    def __eq__(self, o):
        return isinstance(o, Pos) and self.x == o.x and self.y == o.y

    def __abs__(self):
        return abs(self.x)+abs(self.y)

    def dis(self, p):
        return abs(self.x-p.x)+abs(self.y-p.y)


@dataclass
class Tile:

    o: object = None
    p: Pos
    g: int = 0
    h: int = 0

    def __str__(self):
        return str(self.o)
    
    def __eq__(self, o):
        return isinstance(o, Tile) and self.p == o.p
    
    def f(self):
        return self.g + self.h


@dataclass
class Grid:

    def __init__(self, tile_map=[]):

        self.map = {}

        for y, line in enumerate(tile_map):
            for x, tile in enumerate(line):
                if tile != " ":
                    p = Pos(x,y)
                    self.map[p] = tile
                    tile.p = p
        
        for key, cell in self.map.items():
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                k = key+Pos(dx,dy)
                adj = self.map.get(k, None)
                if adj:
                    cell.adj[k] = adj

    def __getitem__(self, k):
        return self.map.get(k, None)
    
    def __setitem__(self, k, v):
        self.map[k] = v 


def a_star(start, end):
    """
    Returns the shortest reversed path from the end to the start.
    """
    # We define the g & h values of the starting and ending nodes
    start.g = end.g = end.h = 0
    start.h = start.dis(end)

    seen = dict()
    seen[start.p] = None

    frontier = [start]

    while not frontier:
        frontier = sorted(frontier, key = lambda n : n.f()).pop(0)
        current = frontier.popleft()

        if current == end:
            break

        G = current.g + 1
        for nxt_p, nxt in current.adj.items():
            if nxt_p not in seen or G < nxt.g:
                nxt.g = G
                seen[nxt_p] = current.p
                frontier.append(nxt)
                if nxt.h == 0:
                    nxt.h = nxt.dis(end)
    
    c = end.p
    path = []
    while c != None:
        path.append(c)
        c = seen[c]
    return path

