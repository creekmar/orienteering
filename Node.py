
from dataclasses import dataclass
from __future__ import annotations
import Calc

@dataclass
class node:
    coor: tuple
    g: float
    h: float
    f: float
    parent: node

    def get_sucessors(self, terrain, elev, width, length, end):
        successors = list()
        x = node.coor[0]
        y = node.coor[1]
        if (x - 1) > -1:
            g = Calc.get_g_estimate(terrain, elev, node.coor, (x - 1, y))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x - 1, y), end)
                successors.append(node((x - 1, y), g, h, g+h, self))
        if (y - 1) > -1:
            g = Calc.get_g_estimate(terrain, elev, node.coor, (x - 1, y))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x, y - 1), end)
                successors.append(node((x, y - 1), g, h, g + h, self))
        if (x + 1) < width:
            g = Calc.get_g_estimate(terrain, elev, node.coor, (x + 1, y))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x + 1, y), end)
                successors.append(node((x + 1, y), g, h, g + h, self))
        if (y + 1) < length:
            g = Calc.get_g_estimate(terrain, elev, node.coor, (x, y + 1))
            if g != -1:
                h = Calc.get_h_estimate(terrain, elev, (x, y + 1), end)
                successors.append(node((x, y + 1), g, h, g + h, self))
        return successors

    def __eq__(self, other):
        if not isinstance(other, node):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.coor == other.coor

    def __hash__(self):
        return str(self.coor)
