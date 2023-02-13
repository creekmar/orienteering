"""
Ming Creekmore
Node class for A* search of orienteering map.
coor: the coordinates of the node
g: the g-cost
h: the estimated h-cost
f: g+h
parent: the string of the parent
distance: the distance traveled to get to the node from
    starting point in meters
"""
from __future__ import annotations
from dataclasses import dataclass
import Calc

@dataclass
class node:
    coor: tuple
    g: float
    h: float
    f: float
    parent: int
    distance: float

    def get_sucessors(self, terrain, elev, width, length, end):
        """
        get the successors of current node - north, east, south, west
        Note: 50 is added to h-cost if it is going the "wrong" direction
        :param terrain: the pixel access image
        :param elev: 2D elevation array
        :param width: dimensions
        :param length:
        :param end: goal coordinate
        :return: set of successors
        """
        successors = set()
        x = self.coor[0]
        y = self.coor[1]
        # to the left
        if (x - 1) > -1:
            dist = Calc.get_distance(elev, self.coor, (x - 1, y))
            g = Calc.get_g_estimate(terrain, elev, self.coor, (x - 1, y))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x - 1, y), end)
                if end[0] - x > 0:
                    h += 50
                successors.add(node((x - 1, y), g, h, g+h, self.__hash__(), dist))
        # to the top
        if (y - 1) > -1:
            dist = Calc.get_distance(elev, self.coor, (x, y - 1))
            g = Calc.get_g_estimate(terrain, elev, self.coor, (x, y - 1))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x, y - 1), end)
                if end[1] - y > 0:
                    h += 50
                successors.add(node((x, y - 1), g, h, g + h, self.__hash__(), dist))
        # to the right
        if (x + 1) < width:
            dist = Calc.get_distance(elev, self.coor, (x + 1, y))
            g = Calc.get_g_estimate(terrain, elev, self.coor, (x + 1, y))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x + 1, y), end)
                if end[0] - x < 0:
                    h += 50
                successors.add(node((x + 1, y), g, h, g + h, self.__hash__(), dist))
        # to the bottom
        if (y + 1) < length:
            dist = Calc.get_distance(elev, self.coor, (x, y + 1))
            g = Calc.get_g_estimate(terrain, elev, self.coor, (x, y + 1))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x, y + 1), end)
                if end[1] - y > 0:
                    h += 50
                successors.add(node((x, y + 1), g, h, g + h, self.__hash__(), dist))
        return successors

    def __eq__(self, other):
        """
        Equal when the coordinates are the same
        :param other: obj to compare to
        :return: true/false
        """
        if not isinstance(other, node):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.coor == other.coor

    def __hash__(self):
        """
        a hash of the two coordinate numbers
        :return:
        """
        return self.coor[0]**2 + self.coor[1]**3
