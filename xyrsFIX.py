__author__ = 'Dustin'

import sys, os, re

for file in os.listdir():
    if re.search("^\d{4}|^\d{3}", file):
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
