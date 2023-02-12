"""
Ming Creekmore
mec5765
Perform A* search to find the shortest distance between two places on a map
"""

from dataclasses import dataclass
from PIL import Image
import sys
import Calc
from Read import elevation

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

        #how to edit pixels, save img, and display
        # for i in range(300):
        #     for j in range(100):
        #         terrain[i,j] = (0,0,0)
        # ter.save(sys.argv[4])
        # ter.show()

    else:
        print("Usage: lab1.py terrain-image elevation-file path-file output-image-filename")


if __name__ == '__main__':
    main()

