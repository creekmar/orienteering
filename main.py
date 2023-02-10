"""
Ming Creekmore
mec5765
Perform A* search to find the shortest distance between two places on a map
"""

from PIL import Image
import sys

def read_terrain(filename):
    with Image.open(filename) as ter:
        terrain = ter.load()
        print(ter)
        print(ter.getbbox())

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

def main():
    if len(sys.argv) == 5:
        print("Wow! You gave the correct arguments.")
        # read_terrain(sys.argv[1])
        with Image.open(sys.argv[1]) as ter:
            box = ter.getbbox()
            width = box[2]-box[0]
            length = box[3]-box[1]
            elev_coor = read_elev_file(sys.argv[2], width, length)

    else:
        print("Usage: lab1.py terrain-image elevation-file path-file output-image-filename")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

