import csv
import os
import re

path = (os.path.dirname(os.path.realpath(__file__)) + r"\input.txt")

with open(path, newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=',')

    total = 0

    for row in rowreader:
        first = re.search(r'\d+', str(row)).group()[0:1]
        reversed_row = str(row) [::-1]
        last = re.search(r'\d+', reversed_row).group()[0:1]
        num = int(first + last)

        total = total + num
    
    print(total)



