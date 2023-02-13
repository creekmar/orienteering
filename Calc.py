"""
Ming Creekmore
mec5765
A file to calculate the g-value and the h-value for an A* search
algorithm that looks for the shortest path between two points
on a map, considering the terrain and elevation
"""

import math

colorset = {"f89412": 5, "ffc000": 14, "ffffff": 8, "02d03c": 10,
                   "028828": 20, "054918": -1, "0000ff": 2000, "473303": 5, "000000": 5,
                   "cd0065": -1}
x_dist = 10.29
y_dist = 7.55

def get_terrain_speed(terrain, x, y):
    """
    Given a Pixel Access Object and coordinates, gives the
    hex color at that coordinate
    :param terrain: pixel access object
    :param x:
    :param y:
    :return: terrain speed
    """

    color = terrain[x, y]
    color_string = ""
    for i in range(3):
        # need to do this because if it won't give the extra 0
        # in front if it is not more than one digit
        hex_num = hex(color[i])[2:]
        if len(hex_num) == 1:
            color_string += "0" + hex_num
        else:
            color_string += hex_num
    return colorset[color_string]

def get_distance(elev, coor1, coor2):
    """
    gets the straight-line distance between coor1 and coor2
    :param elev: 2D array of elevation
    :param coor1:
    :param coor2:
    :return:
    """
    x1 = coor1[1]
    x2 = coor2[1]
    y1 = coor1[0]
    y2 = coor2[0]
    z_dist = math.fabs(elev[x1][y1] - elev[x2][y2])
    if (y2 - y1) != 0:
        distance = math.sqrt(y_dist ** 2 + z_dist ** 2)
    else:
        distance = math.sqrt(x_dist ** 2 + z_dist ** 2)
    return distance

def get_g_estimate(terrain, elev, coor1, coor2):
    """
    Given the Pixel Access Object, elevation file, and two coordinates,
    it will get a g_estimate from the first coor to the second
    coordinate. The g_estimate is the terrain speed * the distance
    :param terrain: Pixel Access Objet
    :param elev: the elevation coordinate 2D array
    :param coor1: first coordinate
    :param coor2: second coordinate
    :return: g-cost which is speed*distance between two coor
    """
    x2 = coor2[1]
    y2 = coor2[0]
    # can we even move to area
    speed = get_terrain_speed(terrain, y2, x2)
    if speed == -1:
        return -1

    distance = get_distance(elev, coor1, coor2)
    return speed*distance

def get_h_estimate(terrain, elev, curr, end):
    """
    Given a Pixel Access Image, elevation file, and start and end
    coor, will return the h-estimate, from the current coor to
    the goal coor. The h-estimate is the distance * speed
    :param terrain: Pixel Access Image
    :param elev: 2D array of elevation values
    :param curr: current coor
    :param end: goal coor
    :return: the h-estimate from current coor to goal coor
    """
    currx = curr[1]
    curry = curr[0]
    endx = end[1]
    endy = end[0]
    # can we even get to pixel
    speed = get_terrain_speed(terrain, curry, currx)
    if speed == -1:
        return -1
    # getting base x,y,z distances
    x_dif = math.fabs(endx-currx)
    y_dif = math.fabs(endy-curry)
    z_dif = math.fabs((elev[currx][curry]-elev[endx][endy]))

    distance = math.sqrt(x_dif**2 + y_dif**2 + z_dif**2)*speed/4
    return distance
