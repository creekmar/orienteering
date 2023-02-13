"""
Ming Creekmore
mec5765
Perform A* search to find the shortest distance between two places on a map
"""

from dataclasses import dataclass
from operator import attrgetter
import time

from PIL import Image
import sys
import Calc
import Read
import Node
from Read import elevation

def get_lowestf(queue):
    """
    Given a list of nodes, will find the node with the lowest f value,
    remove it from the list and return it
    :param queue: list of nodes
    :return: node with lowest f value
    """
    lowest = 0
    for i in range(1, len(queue)):
        if queue[lowest].f > queue[i].f:
            lowest = i
    return queue.pop(i)

def a_star(terrain, elev, start, goal, width, length):
    """
    Given a Pixel Access Object, 2D array of elevations, start coor, goal coor, and
    dimensions, will return the end node of the shortest path between start and goal
    :param terrain: Pixel Access Object
    :param elev: the 2D array of elevation levels
    :param start: start coordinate
    :param goal: goal coordinate
    :param width:
    :param length:
    :return:
    """
    frontier = dict()
    visited = dict()
    found = False
    start_h = Calc.get_h_estimate(terrain, elev, start, goal)
    temp_node = Node.node(start, 0, start_h, start_h, -1, 0)
    frontier[temp_node.__hash__()] = temp_node

    while len(frontier) > 0:
        current = min(frontier.values(), key=attrgetter('f'))
        frontier.pop(current.__hash__())
        if current.coor == goal:
            found = True
            break
        successors = current.get_sucessors(terrain, elev, width, length, goal)
        # add successor if not in frontier and not in visited
        # update cost values if a successor is in frontier and f is less
        for step in successors:
            if step.__hash__() not in visited:
                if step.__hash__() in frontier:
                    other = frontier.pop(step.__hash__())
                    if step.f < other.f:
                        frontier[step.__hash__()] = step
                    else:
                        frontier[step.__hash__()] = other
                else:
                    frontier[step.__hash__()] = step
        visited[current.__hash__()] = current
    # edit map with solution path if found
    distance = 0
    if found:
        path = []
        while current.parent != -1:
            path.append(current)
            distance += current.distance
            current = visited[current.parent]
        path.append(current)
        distance += current.distance
    return distance, path

def main():
    start_time = time.time()
    if len(sys.argv) == 5:
        #read_terrain(sys.argv[1])
        with Image.open(sys.argv[1]) as ter:
            dim = ter.size
            width = dim[0]
            length = dim[1]
            terrain = ter.load()
        elev_coor = elevation(sys.argv[2], width, length)
        dest = Read.dest(sys.argv[3])
        dist = 0
        path = []
        for i in range(len(dest)-1):
            if(len(dest[i+1]) != 2):
                break
            sol = a_star(terrain, elev_coor, dest[i], dest[i+1], width, length)
            dist += sol[0]
            path.extend(sol[1])
        if dist != 0:
            for i in range(len(path)):
                terrain[path[i].coor[0], path[i].coor[1]] = (153, 50, 204)
            # for i in range(len(dest)):
            #     terrain[dest[i][0], dest[i][1]] = (153, 50, 204)
            ter.save(sys.argv[4])
            ter.show()
            print("Distance:", dist, "m")
        else:
            print("No Solution!")

    else:
        print("Usage: lab1.py terrain-image elevation-file path-file output-image-filename")
    print("Time elapsed:",time.time() - start_time)


if __name__ == '__main__':
    main()

