__author__ = 'Dustin'

import sys, os, re

extension = ".out"

# Find file named XXXX.xyrs or XXXX.txt where XXXX is a three or four digit integer (panel number)
# This is generally what I name the XYRS files as I work with them
for file in os.listdir():
    if re.search("^\d{3,}.(xyrs|txt)", file):
        file_in = file
        break

try:
    xyrsIN = open(file_in, 'r')
except IOError:
    print("IO Error")
    exit(2)
except NameError:
    print("XYRS File Not Found")
    exit(1)

# Name output file same as input file but with .out extension
filename_split = file.split(".")
out_filename = "".join([filename_split[0], extension])
xyrsOUT = open(out_filename, 'w')

xyrsIN_list = list(xyrsIN)

# Each capacitor, resistor, diode, and other 3-pin package components need to be offset
# Q designators tend to be the three-pole SOT-23 type components and usually have a different offset.
# TODO: These offset should be tested across a few different panels.
for element in xyrsIN_list:
    if re.search("^(C|R|D)", element):
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
