"""
Ming Creekmore
mec5765
Perform A* search to find the shortest distance between two places on a map
"""

from PIL import Image
import sys
import math

colorset = {"f89412": 5, "ffc000": 10, "ffffff": 20, "02d03c": 30,
                   "028828": 50, "054918": -1, "0000ff": 100, "473303": 5, "000000": 5,
                   "cd0065": -1}
x_dist = 10.29
y_dist = 7.55

def read_terrain(filename):
    with Image.open(filename) as ter:
        terrain = ter.load()
        print(ter.size)

def read_elev_file(filename, width, length):
    """
    Reads the filename and puts it into a 2d array
    Also checks whether the file rows and col match the given width/length
    Assumes: the file is a list and row of decimal numbers
    :param filename: Name of file to read
    :param width: the min width/col that the file needs to have
    :param length: the min length/rows that the file needs to have
    :return: 2D array of all the individual float values in the given file
    """

    elev_coor = list()
    with open(filename) as elev:
        for count, line in enumerate(elev):
            separate_line = [float(n) for n in line.split()]
            if width > len(separate_line):
                sys.exit("Elevation file width is too short to be used for the given terrain image")
            elev_coor.append(separate_line[:width])
        if length > (count+1):
            sys.exit("Elevation file length is too short to be used for the given terrain image")
    return elev_coor

def get_terrain_speed(terrain, row, col):
    """
    Given a Pixel Access Object and coordinates, gives the
    hex color at that coordinate
    :param terrain: pixel access object
    :param x:
    :param y:
    :return: terrain speed
    """

    color = terrain[row,col]
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

def get_g_estimate(terrain, elev, row1, col1, row2, col2):
    """
    Given the Pixel Access Object, elevation file, and two coordinates,
    it will get a g_estimate from the first coor to the second
    coordinate. The g_estimate is the terrain speed * the distance
    :param terrain: Pixel Access Objet
    :param elev: the elevation coordinate 2D array
    :param row1: first coordinate
    :param col1:
    :param row2: second coordinate
    :param col2:
    :return: g-cost which is speed*distance between two coor
    """

    z_dist = elev[row1][col1] - elev[row2][col2]
    speed = get_terrain_speed(terrain, row2, col2)
    if (row2 - row1) != 0:
        distance = math.sqrt(y_dist**2 + z_dist**2)
    else:
        distance = math.sqrt(x_dist**2 + z_dist**2)
    return speed*distance


def main():
    if len(sys.argv) == 5:
        print("Wow! You gave the correct arguments.")
        #read_terrain(sys.argv[1])
        with Image.open(sys.argv[1]) as ter:
            dim = ter.size
            width = dim[0]
            length = dim[1]
            terrain = ter.load()
        elev_coor = read_elev_file(sys.argv[2], width, length)
        print(get_g_estimate(terrain, elev_coor, 100, 100, 101, 100))

    else:
        print("Usage: lab1.py terrain-image elevation-file path-file output-image-filename")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

