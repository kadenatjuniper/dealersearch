import os
import sys
from findWebsite import findWebsite

NAME = 1
CITY = 3
STATE = 4

filename = sys.argv[1]
filein = open(filename)
filein.readline()  # read the headerline

fileout = open('test.csv', 'w')

for line in filein:
    strippedline = line.split('\n')
    splitline = line.split(',')
    search = splitline[NAME].replace(" ", "+").replace('(', '').replace(')', '') + "+" + splitline[CITY].replace(" ", "+") + "+" + splitline[STATE].replace(" ", "+")
    print(search)
    website = findWebsite(search)
    fileout.write(f"{strippedline}, {website}\n")
