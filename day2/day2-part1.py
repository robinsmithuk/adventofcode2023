import csv
import os
import pandas as pd

path = (os.path.dirname(os.path.realpath(__file__)) + r"/day_2_input.txt")

with open(path, newline='') as csvfile:
    rowreader = csv.reader(csvfile, delimiter=';')
    list_of_games = []

    for row in rowreader:
        
        game_num = 0
        game_line = str(row[0])

        if game_line.startswith('Game') == True:
            game_num = int(game_line[game_line.index(' ') + 1:game_line.index(':')])

        for turn in row:
            if turn.startswith('Game') == True:
                rep_turn = str(turn.replace('Game ' + str(game_num) + ':', ''))
            else: 
                rep_turn = turn

            blocks = rep_turn.split(', ')

            for block in blocks:

                num_of_blocks = int(block.strip().split()[0])
                colour_of_blocks = block.strip().split()[1]

                invalid_turn = 0

                if colour_of_blocks == 'red' and num_of_blocks > 12:
                    invalid_turn = 1

                if colour_of_blocks == 'green' and num_of_blocks > 13:
                    invalid_turn = 1

                if colour_of_blocks == 'blue' and num_of_blocks > 14:
                    invalid_turn = 1

                turn_dict = {
                    'game': game_num,
                    'num_of_blocks': num_of_blocks,
                    'colour_of_blocks': colour_of_blocks,
                    'invalid_turn': invalid_turn
                }

                list_of_games.append(turn_dict)

    df = pd.DataFrame(list_of_games)
    game_totals = df.groupby(['game'], as_index = False)['invalid_turn'].sum()

    df2 = game_totals.where(game_totals['invalid_turn'] == 0)
    df2 = df2.dropna(thresh=1)

    total = int(df2['game'].sum())

    print(total)



##ignore below
    #blocks_table = df.pivot_table(['num_of_blocks'], ['game'], 'invalid_turn', fill_value=0, aggfunc='sum')

    #print(blocks_table)

   # red_cond = blocks_table['red'] <= 12
   # green_cond = blocks_table['green'] <= 13
   # blue_cond  = blocks_table['blue'] <= 14

   # df2 = blocks_table.where(red_cond & green_cond & blue_cond)
   # df2 = df2.dropna(thresh=1).reset_index()

   # print(df2)

   # total = df2['game'].sum()

   # print(total)






