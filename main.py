"""
Ming Creekmore
mec5765
Perform A* search to find the shortest distance between two places on a map
"""

from PIL import Image
import sys

def main():
    if len(sys.argv) == 5:
        print("Wow! You gave the correct arguments.")
    else:
        print("Usage: lab1.py terrain-image elevation-file path-file output-image-filename")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

