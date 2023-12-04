import csv
import os
import re

def find_special_characters(input_string):
    pattern = r'[!\"£$%^&*()+_]'
    matches = re.findall(pattern, input_string)
    return matches

def find_numbers_and_positions(input_string):
    pattern = r'\d+'
    matches = re.finditer(pattern, input_string)
    result = [(match.group(), match.start(), match.end()) for match in matches]
    return result

path = (os.path.dirname(os.path.realpath(__file__)) + r"/day_3_input_test.txt")

with open(path, newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=',')

#467..114..
#...*......
#..35..633.
#......#...
#617*......
#.....+.58.
#..592.....
#......755.
#...$.*....
#.664.598..

    sch_rows = []

    for row in rowreader:
        sch_rows.append(row[0])

    row_count = 0

    for row in sch_rows:
 
        pos_matches = find_numbers_and_positions(str(row))

        if pos_matches != None:

            for pos in pos_matches:
                                
                num_pos = {
                    'line': row_count,
                    'value': int(pos[0]),
                    'start': int(pos[1]),
                    'end': int(pos[2]),
                    'is_valid': False
                }

                #Top Row
                if row_count == 0:
                    #Top Left
                    if num_pos['start'] == 0:
                        line_right = str(sch_rows[row_count])[num_pos['end']:num_pos['end'] + 1]
                        line_below = str(sch_rows[row_count + 1])[0:num_pos['end'] + 1]

                        if find_special_characters(line_below) or find_special_characters(line_right):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                    #Top Middle
                    if num_pos['start'] > 0:
                        line_left = str(sch_rows[row_count])[num_pos['start']:num_pos['start'] - 1]
                        line_right = str(sch_rows[row_count])[num_pos['end']:num_pos['end'] + 1]
                        line_below = str(sch_rows[row_count + 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_below) or find_special_characters(line_right) or find_special_characters(line_left):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                    #Top Right
                    if num_pos['end'] == len(row):
                        line_left = str(sch_rows[row_count])[num_pos['start']:num_pos['start'] - 1]
                        line_below = str(sch_rows[row_count + 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_below) or find_special_characters(line_right) or find_special_characters(line_left):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                #Middle Rows
                if row_count > 1 and row_count < len(sch_rows):
                    #Middle Left
                    if num_pos['start'] == 0:
                        line_right = str(sch_rows[row_count])[num_pos['end']:num_pos['end'] + 1]
                        line_below = str(sch_rows[row_count + 1])[num_pos['start'] - 1:num_pos['end'] + 1]
                        line_above = str(sch_rows[row_count - 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_above) or find_special_characters(line_below) or find_special_characters(line_right):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                    #Middle Middle
                    if num_pos['start'] > 0:
                        line_left = str(sch_rows[row_count])[num_pos['start']:num_pos['start'] - 1]
                        line_right = str(sch_rows[row_count])[num_pos['end']:num_pos['end'] + 1]
                        line_below = str(sch_rows[row_count + 1])[num_pos['start'] - 1:num_pos['end'] + 1]
                        line_above = str(sch_rows[row_count - 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_below) or find_special_characters(line_above) or find_special_characters(line_right) or find_special_characters(line_left):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                    #Middle Right
                    if num_pos['end'] == len(row):
                        line_left = str(sch_rows[row_count])[num_pos['start']:num_pos['start'] - 1]
                        line_below = str(sch_rows[row_count + 1])[num_pos['start'] - 1:num_pos['end'] + 1]
                        line_above = str(sch_rows[row_count - 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_below) or find_special_characters(line_above) or find_special_characters(line_left):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                #Bottom Row
                if row_count == len(sch_rows):

                    #Bottom Left
                    if num_pos['start'] == 0:
                        line_right = str(sch_rows[row_count])[num_pos['end']:num_pos['end'] + 1]
                        line_above = str(sch_rows[row_count - 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_above) or find_special_characters(line_right):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                    #Bottom Middle
                    if num_pos['start'] > 0:
                        line_left = str(sch_rows[row_count])[num_pos['start']:num_pos['start'] - 1]
                        line_right = str(sch_rows[row_count])[num_pos['end']:num_pos['end'] + 1]
                        line_above = str(sch_rows[row_count - 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_above) or find_special_characters(line_right) or find_special_characters(line_left):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                    #Bottom Right
                    if num_pos['end'] == len(row):
                        line_left = str(sch_rows[row_count])[num_pos['start']:num_pos['start'] - 1]
                        line_above = str(sch_rows[row_count - 1])[num_pos['start'] - 1:num_pos['end'] + 1]

                        if find_special_characters(line_above) or find_special_characters(line_left):
                            num_pos['is_valid'] = True
                            print('valid')
                        else:
                            print('Invalid')

                #ere
        row_count = row_count + 1   
                        

        


