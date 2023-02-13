"""
Ming Creekmore
mec5765
Perform A* search to find the shortest distance between two places on a map
"""

from dataclasses import dataclass
from operator import attrgetter

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
    frontier = list()
    visited = dict()
    found = False
    start_h = Calc.get_h_estimate(terrain, elev, start, goal)
    temp_node = Node.node(start, 0, start_h, start_h, -1, 0)
    frontier.append(temp_node)

    while len(frontier) > 0:
        current = min(frontier, key=attrgetter('f'))
        frontier.remove(current)
        if current.coor == goal:
            found = True
            break
        successors = current.get_sucessors(terrain, elev, width, length, goal)
        for step in successors:
            if step.__hash__() not in visited:
                print(step)
                if step in frontier:
                    other = frontier.pop(frontier.index(step))
                    if step.f < other.f:
                        frontier.append(step)
                    else:
                        frontier.append(other)
                else:
                    frontier.append(step)
        visited[current.__hash__()] = current
    # edit map with solution path if found
    distance = 0
    if found:
        while current.parent != -1:
            terrain[current.coor[0], current.coor[1]] = (153, 50, 204)
            distance += current.distance
            current = visited[current.parent]
        terrain[current.coor[0], current.coor[1]] = (153, 50, 204)
        distance += current.distance
    return distance

def main():
    if len(sys.argv) == 5:
        print("Wow! You gave the correct arguments.")
        #read_terrain(sys.argv[1])
        with Image.open(sys.argv[1]) as ter:
            dim = ter.size
            width = dim[0]
            length = dim[1]
            terrain = ter.load()
        elev_coor = elevation(sys.argv[2], width, length)
        dest = Read.dest(sys.argv[3])
        for i in range(len(dest)-1):
            dist = a_star(terrain, elev_coor, dest[i], dest[i+1], width, length)
            if dist != 0:
                ter.save(sys.argv[4])
                ter.show()
                print("Distance:", dist, "m")
            else:
                print("No Solution!")

    else:
        print("Usage: lab1.py terrain-image elevation-file path-file output-image-filename")


if __name__ == '__main__':
    main()

