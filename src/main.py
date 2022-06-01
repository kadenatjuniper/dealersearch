import os
import sys
from findWebsite import findWebsite
from keywordCheck import keywordCheck

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
    if website:
        topcon = keywordCheck(website, 'topcon')
        sokkia = keywordCheck(website, 'sokkia')
    else:
        topcon = None
        sokkia = None
    fileout.write(f"{strippedline}, {website}, {topcon}, {sokkia}\n")
