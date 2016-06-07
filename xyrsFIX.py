__author__ = 'Dustin'

import sys, os, re

# Find file named XXXX.xyrs or XXXX.txt where XXXX is a three or four digit integer (panel number)
# This is generally what I name the XYRS files as I work with them
for file in os.listdir():
    if re.search("^\d{3,}.(xyrs|txt)", file):
        file_in = file

try:
    xyrsIN = open(file_in, 'r')
except IOError:
    print("IO Error")
    exit(2)
except NameError:
    print("XYRS File Not Found")
    exit(1)

xyrsOUT = open('xyrs.out', 'w')

xyrsIN_list = list(xyrsIN)

# Each capacitor, resistor, diode, and other 3-pin package components need to be offset
# Q designators tend to be the three-pole SOT-23 type components and usually have a different offset.
# TODO: These offset should be tested across a few different panels.
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
