import csv
import os
import re
import pandas as pd
import numpy as np


path = (os.path.dirname(os.path.realpath(__file__)) + r"/day2_input_test.txt")

with open(path, newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    list_of_games = []

    for row in rowreader:
        
        game_num = 0
        game_line = str(row[0])

        if game_line.startswith('Game') == True:
            game_num = int(game_line[game_line.index(' ') + 1:game_line.index(':')])

#Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

        for turn in row:
            if turn.startswith('Game') == True:
                rep_turn = str(turn.replace('Game ' + str(game_num) + ':', ''))
            else: 
                rep_turn = turn

            blocks = rep_turn.split(', ')

            for block in blocks:

                turn_dict = {
                    'game': game_num,
                    'num_of_blocks': int(block.strip().split()[0]),
                    'colour_of_blocks': block.strip().split()[1]
                }

                list_of_games.append(turn_dict)

    df = pd.DataFrame(list_of_games)
    game_totals = df.groupby(['game','colour_of_blocks'])['num_of_blocks'].sum()

# The Elf would first like to know which games would 
# have been possible if the bag contained only
# 12 red cubes, 13 green cubes, and 14 blue cubes?

    red_total = 12
    green_total = 13
    blue_total = 14

    red_games = game_totals.where(game_totals[2] <= red_total)


    print(df2)





