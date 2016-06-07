__author__ = 'Dustin'

import sys

try:
    file_in = sys.argv[1]
except IndexError:
    print("Syntax: \"xyrsFIX.py <file>\" where <file> is the input XYRS")
    exit(1)

try:
    xyrsIN = open(file_in, 'r')
except IOError:
    print("IO Error; File not Found")
    exit(1)
    
xyrsOUT = open('xyrs.out', 'w')

xyrsIN_list = list(xyrsIN)

for element in xyrsIN_list:
    if element[0] == 'C':
        strsplit = element.split("\t")
        strsplit[3] = str(int(strsplit[3]) - 90)
        strsplit = "\t".join(strsplit)
        element = strsplit
    elif element[0] == 'R':
        strsplit = element.split("\t")
        strsplit[3] = str(int(strsplit[3]) - 90)
        strsplit = "\t".join(strsplit)
        element = strsplit
    elif element[0] == 'D':
        strsplit = element.split("\t")
        strsplit[3] = str(int(strsplit[3]) - 90)
        strsplit = "\t".join(strsplit)
        element = strsplit
    elif element[0] == 'Q':
        strsplit = element.split("\t")
        strsplit[3] = str(int(strsplit[3]) + 90)
        strsplit = "\t".join(strsplit)
        element = strsplit
    xyrsOUT.write(element)
