"""
Ming Creekmore
Reads input files: elevation, path
"""

import sys

def elevation(filename, width, length):
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

def dest(filename):
    """
    Given a filename, will read the coordinates in the file and
    return it as a list of tuples. These represent the coor
    to start and visit/end
    :param filename:
    :return: list of 2 element tuples (coor)
    """
    goals = list()
    with open(filename) as p:
        for line in p:
            goals.append(tuple(line.split()))
    return goals
