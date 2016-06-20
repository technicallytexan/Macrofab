import os
import re

__author__ = 'Dustin'

extension = ".out"

# Find file named XXXX.xyrs or XXXX.txt where XXXX is a three (or more) digit integer (panel number)
# This is generally what I name the XYRS files as I work with them
for file in os.listdir(os.getcwd()):
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
out_filename = filename_split[0] + extension
xyrsOUT = open(out_filename, 'w')
output_log = open("out.log", 'w')

print("Input panel size: ")
panel_size = str(input())

xyrsOUT.write("".join([filename_split[0], "\n"]))

xyrsIN_list = list(xyrsIN)

# Each capacitor, resistor, diode, and other 3-pin package components need to be offset
# Adjusted for clockwise/counter-clockwise inconsistency
# TODO: These offset should be tested across a few different panels.
for element in xyrsIN_list:
    strsplit = element.split("\t")
    if re.search("(U|IC)\$?\d+", strsplit[0]):
        if re.search("(270|90)", strsplit[3]):
            strsplit[3] = int(strsplit[3]) + 180
            if strsplit[3] >= 360:
                strsplit[3] = int(strsplit[3]) - 360
            strsplit[3] = str(strsplit[3])
    else:
        if re.search("(270|90)", strsplit[3]):
            strsplit[3] = str(int(strsplit[3]) + 90)
        else:
            strsplit[3] = str(int(strsplit[3]) - 90)
        strsplit = "\t".join(strsplit)
        element = strsplit
        output_log.write(element)
    xyrsOUT.write(element)
xyrsOUT.write("\n")
if re.search("5", panel_size):
    xyrsOUT.write("FID1\t130\t2505\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID2\t4880\t1005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID3\t4880\t4005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID1\t130\t2505\t0\t2\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID2\t4880\t1005\t0\t2\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID3\t4880\t4005\t0\t2\t1\t40\t40\tFID\tFID\n")
elif re.search("12", panel_size):
    xyrsOUT.write("FID1\t130\t6005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID2\t11880\t1005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID3\t11880\t11005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID1\t130\t6005\t0\t2\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID2\t11880\t1005\t0\t2\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID3\t11880\t11005\t0\t2\t1\t40\t40\tFID\tFID\n")
elif re.search("16", panel_size):
    xyrsOUT.write("FID1\t130\t8005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID2\t15880\t1005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID3\t15880\t15005\t0\t1\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID1\t130\t8005\t0\t2\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID2\t15880\t1005\t0\t2\t1\t40\t40\tFID\tFID\n")
    xyrsOUT.write("FID3\t15880\t15005\t0\t2\t1\t40\t40\tFID\tFID\n")

xyrsIN.close()
xyrsOUT.close()
output_log.close()
