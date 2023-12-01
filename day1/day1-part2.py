import csv
import os
import re

path = (os.path.dirname(os.path.realpath(__file__)) + r"\input.txt")

with open(path, newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=',')

    total = 0

    for row in rowreader:

        cleansed = str(row[0]).replace('twone', 'twoone').replace('sevenine', 'sevennine').replace('oneight', 'oneeight').replace('eightwo','eighttwo').replace('eighthree','eightthree')
        replaced_row = cleansed.replace('seven', '7', 1).replace('nine', '9', 1).replace('three', '3', 1).replace('eight', '8', 1).replace('two', '2', 1).replace('one', '1', 1).replace('four', '4', 1).replace('five', '5', 1).replace('six', '6', 1)

        first = re.search(r'\d+', str(replaced_row)).group()[0:1]
        reversed_row = str(replaced_row) [::-1]

        replaced_reversed_row = reversed_row.replace('one'[::-1], '1', 1).replace('two'[::-1], '2', 1).replace('eight'[::-1], '8', 1).replace('three'[::-1], '3', 1).replace('nine'[::-1], '9', 1).replace('seven'[::-1], '7', 1).replace('four'[::-1], '4', 1).replace('five'[::-1], '5', 1).replace('six'[::-1], '6', 1)
    
        last = re.search(r'\d+', replaced_reversed_row).group()[0:1]
        num = int(first + last)

        total = total + num

    print(total)
